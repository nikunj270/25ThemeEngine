class Tags:
    """Global production tags for SCADA.

    Add new process tags here for PLC/OPC mapping and alarm checks.

    Example:
        FlowRate = 0.0
        Level = 0.0

    Then read values in OPC/opcworker.py and register alarm thresholds in core/alarms.py.
    """


    # Motor= 'ns=3;s="M2Status"."bMasterd"'
    # Motor_Start = 'ns=3;s="M2Status"."bMasterd"'
    # Temperature = 'ns=3;s="M2Status"."r32CurrentBit"'
    # Pressure = 'ns=3;s="M2Status"."tAG1"'"0"

    Motor= False
    Motor_Start = False
    Temperature = 0.0
    Pressure = 0

    # FUTURE TAGS: add new machine/zone variables below
    # FlowRate = 0.0
    # Level = 0.0
