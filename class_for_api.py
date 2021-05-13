from pydantic import BaseModel
import typing as t

class Value_churn(BaseModel):
    AccountWeeks: t.Union[float, int]
    DataUsage: t.Union[float, int]
    CustServCalls: t.Union[float, int]
    DayMins: t.Union[float, int]
    DayCalls: t.Union[float, int]
    MonthlyCharge: t.Union[float, int] 
    OverageFee: t.Union[float, int]
    RoamMins: t.Union[float, int]
    ContractRenewal_yes: t.Union[float, int]
    DataPlan_Yes: t.Union[float, int]

class Batch_Value_Churn(BaseModel):
    BatchValue: t.List[Value_churn]
