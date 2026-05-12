from datetime import datetime, timedelta
from functools import partial
from types import SimpleNamespace
from PySide6.QtCore import QDate, QTimer
from pathlib import Path
import sqlite3
from PySide6.QtWidgets import (
    QFileDialog,
    QDateEdit,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
from OPC.opc_client import OPCClient
from Tag.tags import Tags
from OPC.nodes import *
from OPC import nodes
from reports.generate_pdf_report import (
    alarm_summary_rows,
    load_alarm_rows,
    load_tag_rows,
    production_rows,
    draw_batch_report,
    draw_daily_production_report,
)
from matplotlib.backends.backend_pdf import PdfPages

class UIController:
    def __init__(self, ui, plc_client=None):
        self.ui = ui
        self.plc_client = plc_client  # Access PLC client from UI
        self._log_buffer = ""
        self.setup_report_page()
        self.setup_connections()
        self._cursor_visible = True
        self._log_buffer = "" #Store log seperately
        self._cursor_timer = QTimer()
        self._cursor_timer.timeout.connect(self._toggle_cursor_visibility)
        self._cursor_timer.start(5000)  # Toggle cursor every 500 ms
        self.is_user_editing = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.read_plc_values)
        self.timer.start(250)

    # ---------------------------------
    # Button Connections HERE ✅
    # ---------------------------------
    def setup_connections(self):
        
        leftcomp = self.ui.leftSidebarComponentContainer.component
        bodycomp = self.ui.MainBodyComponentContainer.component

        mapping = {
            "homeBtn": ("page1", "Home button clicked!"),
            "messageBtn": ("page2", "Message button clicked!"),
            "integrationBtn" : ("page3", "Integration button clicked!"),
            "financeBtn" : ("page4", "Finance button clicked!")

           }

        for button_name, (page_name,msg) in mapping.items():
            button = getattr(leftcomp, button_name)
            page = getattr(bodycomp, page_name)
            button.clicked.connect(
                partial(self.switch_page, page, msg)
            )

        report_btn = getattr(leftcomp, "threadsBtn", None)
        report_page = getattr(bodycomp, "page7", None)
        if report_btn and report_page:
            report_btn.clicked.connect(
                partial(self.switch_page, report_page, "Report button clicked!")
            )

        page6_report_btn = getattr(bodycomp, "pushButton2", None)
        if page6_report_btn and report_page:
            page6_report_btn.setText("Report")
            page6_report_btn.clicked.connect(
                partial(self.switch_page, report_page, "Report page opened!")
            )
            
        Mmapping = {
            "BtnRecycle" : ("page3", "Recycle button clicked!"),
            "BtnReuse" : ("page4", "Reuse button clicked!"),
            "recprevBtn" : ("page3", "Button 3 clicked!"),
            "recnextBtn" : ("page4", "Button 4 clicked!"),
            "pNextBtn" : ("page6", "Button 5 clicked!"),
           }
        
        for button_name, (page_name,msg) in Mmapping.items():
            button = getattr(bodycomp, button_name)
            page = getattr(bodycomp, page_name)
            
            button.clicked.connect(
                partial(self.switch_page, page, msg)
            )

        recmapping = {
            "rec1Btn" : ("page5", 1),  
            "rec2Btn" : ("page5", 2),
            "rec3Btn" : ("page5", 3),
            "rec4Btn" : ("page5", 4),
            "rec5Btn" : ("page5", 5),
            "rec6Btn" : ("page5", 6),
            "rec7Btn" : ("page5", 7),
            "rec8Btn" : ("page5", 8),
            "rec9Btn" : ("page5", 9),
            "rec10Btn" : ("page5", 10),
            "rec11Btn" : ("page5", 11),
            "rec12Btn" : ("page5", 12),
            "rec13Btn" : ("page5", 13),
            "rec14Btn" : ("page5", 14),
        }
        # rec1_button = getattr(bodycomp, "rec1Btn", None)

        for button_name, (page_name,recipe_no) in recmapping.items():
            button = getattr(bodycomp, button_name, None)
            page = getattr(bodycomp, page_name, None)            
            if button and page:
                button.clicked.connect(partial(self.load_recipe_to_page5, recipe_no))

        getattr(bodycomp, "saveRecipeBtn", None).clicked.connect(
            partial(self.update_recipe)  # Assuming you want to update recipe 1 for now
        )

        pbOn = getattr(bodycomp, "pbOnBtn", None)
        pbOff = getattr(bodycomp, "pbOffBtn", None)
        togBtn = getattr(bodycomp, "togBtn", None)
        invBtn = getattr(bodycomp, "invBtn", None)

        togBtn.clicked.connect(
            lambda: self.plc_client.write_bool(nodes.M2_mastered, not Tags.M2bool))
        invBtn.clicked.connect(
            lambda: self.plc_client.write_bool(nodes.M3_mastered, not Tags.M3bool))
        
        if pbOn and self.plc_client:
            pbOn.clicked.connect(
                lambda: self.plc_client.write_bool(nodes.M1_mastered, True))

        if pbOff and self.plc_client:
            pbOff.clicked.connect(
                lambda: self.plc_client.write_bool(nodes.M1_mastered, False))

        bodycomp.ioReal.textEdited.connect(self.user_started_editing)
        bodycomp.ioReal.editingFinished.connect(self.user_finished_editing)
        bodycomp.ioReal.editingFinished.connect(
            lambda: self.plc_client.write_real(nodes.M2_current_bit, float(bodycomp.ioReal.text().split()[0]))
        )
        bodycomp.ioInt.textEdited.connect(self.user_started_editing)
        bodycomp.ioInt.editingFinished.connect(self.user_finished_editing)
        bodycomp.ioInt.editingFinished.connect(
            lambda: self.plc_client.write_int16(nodes.M2_tag1, int(bodycomp.ioInt.text()))
        )
        # if rec1_button:
        #     rec1_button.clicked.connect(
        #         partial(self.load_recipe_to_page5, 1)
        #     )


    def read_plc_values(self):
        # print("Reading PLC values... M1ON")

        self.update_label()
        #self.update_motor_status_label()
        #self.update_tag1_label()
    
    def update_label(self): 
        bodycomp = self.ui.MainBodyComponentContainer.component
        #print("UpdateTags")
        # bodycomp.pbOnBtn.clicked.connected(OPCClient.write_bool(tags.M1bool, True) )
        # bodycomp.pbOffBtn.clicked.connected(OPCClient.write_bool(tags.M1bool, False))
        #print(Tags.M1bool)
        #print(f"Tag M1bool value: {OPCClient.read_bool(tags.Tags.M1bool)}")
        color = "green" if Tags.M1bool else "red"
        bodycomp.pbLbl.setStyleSheet(
            f"background-color: {color}; border-radius: 10px; padding: 1px; "
            f"min-width: 20px; min-height: 20px; max-width: 20px; max-height: 20px;"
        )

        color1 = "green" if Tags.M2bool else "red"
        bodycomp.togLbl.setStyleSheet(
            f"background-color: {color1}; border-radius: 10px; padding: 1px; "
            f"min-width: 20px; min-height: 20px; max-width: 20px; max-height: 20px;"
        )

        color2 = "green" if Tags.M3bool else "red"
        bodycomp.invLbl.setStyleSheet(
            f"background-color: {color2}; border-radius: 10px; padding: 1px; "
            f"min-width: 20px; min-height: 20px; max-width: 20px; max-height: 20px;"
        )

        
        bodycomp.oReal.setText(f"{float(Tags.M2real):.2f} °C")

        if not self.is_user_editing:
            bodycomp.ioReal.setText(f"{float(Tags.M2real):.2f} °C")

        bodycomp.oInt.setText(f"{int(Tags.M2int1)}")

        if not self.is_user_editing:
            bodycomp.ioInt.setText(f"{int(Tags.M2int1)}")   

        # self.ui.label_9.setText(f"{tags.Temperature} °C") #self.ui.label_9.setText(f"{value} °C")
        # self.ui.InputField.setText(f"{float(Tags.Temperature):.2f}") #self.ui.InputField.setText(f"{float(Tags.Temperature):.2f}")
        # if not self.is_user_editing:
        #     self.ui.IOField.setText(f"{float(Tags.Temperature):.2f}") #self.ui.IOField.setText(f"{float(Tags.Temperature):.2f}")

        # self.ui.tag1rf.setText(f"{int(Tags.Pressure)}")
        # if not self.is_user_editing:
        #     self.ui.tag1wrf.setText(f"{int(Tags.Pressure)}")  

        # self.ui.ledstatus.setStyleSheet("border-radius: 10px; background-color: {};".format("green" if Tags.Motor else "red"))
        # if Tags.Motor:
        #     self.ui.mixvalve.setPixmap(QPixmap("Source/Images/GreenValve.png"))
        # else:
        #     self.ui.mixvalve.setPixmap(QPixmap("Source/Images/RedValve.png"))      

    # -------------------------------
    # Navigation Handler
    # -------------------------------
    def switch_page(self, page, message):
        self.ui.MainBodyComponentContainer.component.MainStack.setCurrentWidget(page)

    # -------------------------------
    # Page 7 Report Preview / Export
    # -------------------------------
    def setup_report_page(self):
        bodycomp = self.ui.MainBodyComponentContainer.component
        if hasattr(bodycomp, "page7"):
            return

        page = QWidget()
        page.setObjectName("page7")
        bodycomp.page7 = page

        root = QVBoxLayout(page)
        root.setContentsMargins(12, 12, 12, 12)
        root.setSpacing(10)

        title = QLabel("Batch & Daily Production Report")
        title.setStyleSheet("font-size: 20px; font-weight: 600; color: #222;")
        root.addWidget(title)

        controls = QGroupBox("Select Date Range")
        controls.setStyleSheet(
            "QGroupBox { font-weight: 600; border: 1px solid #c8c8c8; margin-top: 8px; padding: 10px; }"
            "QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 4px; }"
        )
        form = QGridLayout(controls)
        form.setHorizontalSpacing(10)
        form.setVerticalSpacing(8)

        today = QDate.currentDate()
        bodycomp.reportFromDate = QDateEdit(today.addDays(-7))
        bodycomp.reportToDate = QDateEdit(today)
        for date_edit in (bodycomp.reportFromDate, bodycomp.reportToDate):
            date_edit.setCalendarPopup(True)
            date_edit.setDisplayFormat("yyyy-MM-dd")

        bodycomp.reportBatchNumber = QLineEdit("490322")
        bodycomp.reportAccount = QLineEdit("Terminal 0988")
        bodycomp.reportDate = QDateEdit(today)
        bodycomp.reportDate.setCalendarPopup(True)
        bodycomp.reportDate.setDisplayFormat("yyyy-MM-dd")
        bodycomp.reportShift = QLineEdit("A")
        bodycomp.reportMachineName = QLineEdit("Machine 1")
        bodycomp.reportAvailableTime = QLineEdit("480 min")
        bodycomp.reportOee = QLineEdit("0%")

        form.addWidget(QLabel("From"), 0, 0)
        form.addWidget(bodycomp.reportFromDate, 0, 1)
        form.addWidget(QLabel("To"), 0, 2)
        form.addWidget(bodycomp.reportToDate, 0, 3)
        form.addWidget(QLabel("Batch No."), 1, 0)
        form.addWidget(bodycomp.reportBatchNumber, 1, 1)
        form.addWidget(QLabel("Account"), 1, 2)
        form.addWidget(bodycomp.reportAccount, 1, 3)
        form.addWidget(QLabel("Report Date"), 2, 0)
        form.addWidget(bodycomp.reportDate, 2, 1)
        form.addWidget(QLabel("Shift"), 2, 2)
        form.addWidget(bodycomp.reportShift, 2, 3)
        form.addWidget(QLabel("Machine"), 3, 0)
        form.addWidget(bodycomp.reportMachineName, 3, 1)
        form.addWidget(QLabel("Available Time"), 3, 2)
        form.addWidget(bodycomp.reportAvailableTime, 3, 3)
        form.addWidget(QLabel("OEE"), 4, 0)
        form.addWidget(bodycomp.reportOee, 4, 1)

        button_row = QHBoxLayout()
        button_row.addStretch()
        bodycomp.showReportBtn = QPushButton("Show Report")
        bodycomp.exportReportPdfBtn = QPushButton("Export PDF")
        bodycomp.exportReportPdfBtn.setEnabled(False)
        for button in (bodycomp.showReportBtn, bodycomp.exportReportPdfBtn):
            button.setMinimumHeight(34)
            button.setStyleSheet(
                "QPushButton { background: #2f6fbd; color: white; border: 0; border-radius: 4px; padding: 6px 14px; }"
                "QPushButton:disabled { background: #9fb7d6; }"
                "QPushButton:hover:!disabled { background: #245995; }"
            )
        button_row.addWidget(bodycomp.showReportBtn)
        button_row.addWidget(bodycomp.exportReportPdfBtn)
        form.addLayout(button_row, 4, 2, 1, 2)
        root.addWidget(controls)

        bodycomp.reportScrollArea = QScrollArea()
        bodycomp.reportScrollArea.setWidgetResizable(True)
        bodycomp.reportScrollArea.setStyleSheet("QScrollArea { border: 1px solid #d0d0d0; background: white; }")
        bodycomp.reportPreviewHost = QWidget()
        bodycomp.reportPreviewLayout = QVBoxLayout(bodycomp.reportPreviewHost)
        bodycomp.reportPreviewLayout.setContentsMargins(12, 12, 12, 12)
        bodycomp.reportPreviewLayout.setSpacing(14)
        bodycomp.reportPreviewLayout.addWidget(QLabel("Select From/To date, then click Show Report."))
        bodycomp.reportPreviewLayout.addStretch()
        bodycomp.reportScrollArea.setWidget(bodycomp.reportPreviewHost)
        root.addWidget(bodycomp.reportScrollArea, 1)

        bodycomp.showReportBtn.clicked.connect(self.show_report_preview)
        bodycomp.exportReportPdfBtn.clicked.connect(self.export_report_pdf)
        bodycomp.MainStack.addWidget(page)

    def _report_args(self):
        bodycomp = self.ui.MainBodyComponentContainer.component
        from_date = bodycomp.reportFromDate.date().toString("yyyy-MM-dd")
        to_date = bodycomp.reportToDate.date().toString("yyyy-MM-dd")
        return SimpleNamespace(
            db="Database/alarms.db",
            output="reports/batch_daily_report.pdf",
            report="both",
            from_time=f"{from_date} 00:00:00",
            to_time=f"{to_date} 23:59:59",
            batch_number=bodycomp.reportBatchNumber.text().strip() or "490322",
            account=bodycomp.reportAccount.text().strip() or "Terminal 0988",
            report_date=bodycomp.reportDate.date().toString("yyyy-MM-dd"),
            shift=bodycomp.reportShift.text().strip(),
            machine_name=bodycomp.reportMachineName.text().strip(),
            available_time=bodycomp.reportAvailableTime.text().strip(),
            oee=bodycomp.reportOee.text().strip(),
            rows=16,
        )

    def _load_report_data(self, args):
        db_path = Path(args.db)
        if not db_path.exists():
            raise FileNotFoundError(f"Database not found: {db_path}")
        with sqlite3.connect(db_path) as conn:
            alarm_rows = load_alarm_rows(conn, args.from_time, args.to_time)
            tag_rows = load_tag_rows(conn, args.from_time, args.to_time)
        return alarm_rows, tag_rows

    def _clear_preview(self):
        bodycomp = self.ui.MainBodyComponentContainer.component
        layout = bodycomp.reportPreviewLayout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def show_report_preview(self):
        bodycomp = self.ui.MainBodyComponentContainer.component
        if bodycomp.reportFromDate.date() > bodycomp.reportToDate.date():
            QMessageBox.warning(None, "Invalid Date Range", "From date must be before To date.")
            return

        args = self._report_args()
        try:
            alarm_rows, tag_rows = self._load_report_data(args)
        except Exception as exc:
            QMessageBox.critical(None, "Report Error", str(exc))
            return

        self._last_report_args = args
        self._last_alarm_rows = alarm_rows
        self._last_tag_rows = tag_rows
        self._clear_preview()

        summary_title = QLabel(
            f"Batch Report | {args.from_time} to {args.to_time} | Batch {args.batch_number}"
        )
        summary_title.setStyleSheet("font-size: 16px; font-weight: 600;")
        bodycomp.reportPreviewLayout.addWidget(summary_title)

        if alarm_rows:
            headers = ["Group", "# Alarms", "Active", "Cleared", "Acked", "Stoppage Min."]
        else:
            headers = ["Tag", "# Samples", "Min Value", "Max Value", "Avg Value", "Stoppage Min."]
        summary_data = alarm_summary_rows(alarm_rows, tag_rows)
        self._add_preview_table(headers, summary_data or [["No records", 0, 0, 0, 0, "0.0"]])

        production_title = QLabel("Daily Machine Production Report")
        production_title.setStyleSheet("font-size: 16px; font-weight: 600; margin-top: 8px;")
        bodycomp.reportPreviewLayout.addWidget(production_title)

        production_headers = [
            "Speed", "Work Order No.", "Size", "Total No.", "Total Kgs",
            "Set-up & Change over", "Material Not Available", "Less Manpower",
            "Others", "Mechanical Problem", "Electrical Problem", "Material Shifting",
            "Sample Check", "Total stoppage Minutes", "Working Time Minutes",
            "Target Production", "Rej. Nos.",
        ]
        self._add_preview_table(production_headers, production_rows(alarm_rows, tag_rows, 16), min_width=1500)
        bodycomp.reportPreviewLayout.addStretch()
        bodycomp.exportReportPdfBtn.setEnabled(True)
        self.log_to_console(f"Report preview loaded. Alarm rows: {len(alarm_rows)}, Tag rows: {len(tag_rows)}")

    def _add_preview_table(self, headers, rows, min_width=900):
        bodycomp = self.ui.MainBodyComponentContainer.component
        table = QTableWidget(len(rows), len(headers))
        table.setHorizontalHeaderLabels(headers)
        table.setMinimumWidth(min_width)
        table.setMinimumHeight(min(520, 95 + (len(rows) * 32)))
        table.setAlternatingRowColors(True)
        table.setStyleSheet(
            "QHeaderView::section { background: #555; color: white; font-weight: 600; padding: 6px; }"
            "QTableWidget { gridline-color: #cfcfcf; background: white; alternate-background-color: #f7f7f7; }"
        )
        for row_index, row in enumerate(rows):
            for col_index, value in enumerate(row):
                table.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        table.resizeColumnsToContents()
        bodycomp.reportPreviewLayout.addWidget(table)

    def export_report_pdf(self):
        args = getattr(self, "_last_report_args", None)
        if args is None:
            self.show_report_preview()
            args = getattr(self, "_last_report_args", None)
            if args is None:
                return

        default_name = Path("reports") / f"batch_daily_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        output, _ = QFileDialog.getSaveFileName(
            None,
            "Export PDF Report",
            str(default_name),
            "PDF Files (*.pdf)",
        )
        if not output:
            return

        try:
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with PdfPages(output_path) as pdf:
                draw_batch_report(pdf, args, self._last_alarm_rows, self._last_tag_rows)
                draw_daily_production_report(pdf, args, self._last_alarm_rows, self._last_tag_rows)
            QMessageBox.information(None, "PDF Exported", f"Report exported:\n{output_path}")
            self.log_to_console(f"PDF report exported: {output_path}")
        except Exception as exc:
            QMessageBox.critical(None, "Export Error", str(exc))

    #--------------------------------
    def user_started_editing(self,text):
        self.is_user_editing = True
        self.update_edit_status()

    def user_finished_editing(self):
        self.is_user_editing = False
        self.update_edit_status()

    def update_edit_status(self):
        "True" if self.is_user_editing else "False"
        # print(f"User Editing: {status}")    

    def load_recipe_to_page5(self, recipe_no):

        bodycomp = self.ui.MainBodyComponentContainer.component
        recipe_page = getattr(bodycomp, "page5", None)

        if recipe_page is None:
            print("Recipe page not found!")
            return

        db_path = Path(__file__).resolve().parent.parent / "Database" / "recipe.db"
        if not db_path.exists():
            print(f"Database not found at {db_path}")
            return
        
        try:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "SELECT * FROM recipe WHERE srno = ?", (recipe_no,))
                row = cursor.fetchone()
        except Exception as e:
            print(f"Database read error: {e}")
                
        if not row:
            print(f"No recipe found with ID {recipe_no}")
            return
        
        bodycomp.setRecNo.setText(str(row[1]))
        bodycomp.setSprinklerON.setText(str(row[2]))
        bodycomp.setMagON.setText(str(row[3]))
        bodycomp.setMagOFF.setText(str(row[4]))

        self.switch_page(recipe_page, f"Recipe {recipe_no} loaded")
        self.log_to_console(f"Recipe {recipe_no} loaded to page5.")
       
    def update_recipe(self):
        bodycomp = self.ui.MainBodyComponentContainer.component
        
        db_path = Path(__file__).resolve().parent.parent / "Database" / "recipe.db"
        if not db_path.exists():
            print(f"Database not found at {db_path}")
            return
            
        # try:
        #     with sqlite3.connect(db_path) as conn:
        #         cursor = conn.cursor()
        #         cursor.execute(
        #             "UPDATE * FROM recipe WHERE srno = ?", (recipe_no,))
        #         row = cursor.fetchone()
        # except Exception as e:
        #     print(f"Database read error: {e}")
                
        # if not row:
        #     print(f"No recipe found with ID {recipe_no}")
        #     return
        
        recno = bodycomp.setRecNo.text()
        spron = bodycomp.setSprinklerON.text()
        magon = bodycomp.setMagON.text()
        magoff = bodycomp.setMagOFF.text()

        try:
            print(f"Updating recipe {recno} with values: SprinklerTime={spron}, MagnetronOn={magon}, MagnetronOff={magoff}")
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE recipe SET srno=?, SprinklerTime=?, MagnetronOn=?, MagnetronOff=? WHERE srno=?",
                    (recno, spron, magon, magoff, recno)
                )
                conn.commit()
        except Exception as e:
            print(f"Database update error: {e}")
            return
        
      
    # -------------------------------
    # Logging Function
    # -------------------------------
    def log_to_console(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"{'-'*7}\n[{timestamp}] {message}{'-'*2}\n"

        self._log_buffer += formatted_message

        console = self.ui.MainBodyComponentContainer.component.consoleOutput
        console.setPlainText(self._log_buffer + " ")

        # Auto scroll
        console.verticalScrollBar().setValue(console.verticalScrollBar().maximum())
    
    
    def _toggle_cursor_visibility(self):
        console = self.ui.MainBodyComponentContainer.component.consoleOutput

        if self._cursor_visible:
            console.setPlainText(self._log_buffer + " ")  # Show ccrsor
        else:
            console.setPlainText(self._log_buffer + " ")  # Hide cursor

        self._cursor_visible = not self._cursor_visible
        console.verticalScrollBar().setValue(console.verticalScrollBar().maximum())  # Auto-scroll to bottom
     
