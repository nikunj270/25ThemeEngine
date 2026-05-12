class Tags:
    """Global production tags for SCADA.

    Add new process tags here for PLC/OPC mapping and alarm checks.

    Example:
        FlowRate = 0.0
        Level = 0.0

    Then read values in OPC/opcworker.py and register alarm thresholds in core/alarms.py.
    """

    M1bool = False
    M2bool = False
    M3bool = False
    
    M1real = 0.0
    M2real = 0.0

    M2int1 = 0
    M2int2 = 0
   # FUTURE TAGS: add new machine/zone variables below
    # FlowRate = 0.0
    # Level = 0.0
