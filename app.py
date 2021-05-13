from fastapi import FastAPI
from pydantic import BaseModel
import config
import joblib
import typing as t
import numpy as np
from class_for_api import Value_churn, Batch_Value_Churn

LIGHT_GBM_CHURN = joblib.load(config.name_model)

app = FastAPI()

@app.get("/")
def read_message():
    return {"Message": "Hello World"}

@app.get("/article/{number}")
def fonction_carre(number: int = 5, message: str = None):
    return {"carre": number**2, "cube": number**3, "message": message}


@app.get("/prediction/churn_get")
def pred_churn(AccountWeeks: t.Union[float, int], DataUsage: t.Union[float, int], CustServCalls: t.Union[float, int], DayMins: t.Union[float, int],
               DayCalls: t.Union[float, int], MonthlyCharge: t.Union[float, int], OverageFee: t.Union[float, int], RoamMins: t.Union[float, int], ContractRenewal_yes: t.Union[float, int],
               DataPlan_Yes: t.Union[float, int]):

    sample = [AccountWeeks, DataUsage, CustServCalls,
              DayMins, DayCalls, MonthlyCharge,
              OverageFee, RoamMins, ContractRenewal_yes,
              DataPlan_Yes]

    np_sample = np.array(sample)

    prediction = LIGHT_GBM_CHURN.predict(np_sample.reshape(1, -1))

    return {"prediction": "churn" if prediction == 0 else "no-churn"}

@app.post("/prediction/churn_post")
def pred_churn_posth(dict_churn: Value_churn):
    AccountWeeks = dict_churn.AccountWeeks
    DataUsage = dict_churn.DataUsage
    CustServCalls = dict_churn.CustServCalls
    DayMins = dict_churn.DayMins
    DayCalls = dict_churn.DayCalls
    MonthlyCharge = dict_churn.MonthlyCharge
    OverageFee = dict_churn.OverageFee
    RoamMins = dict_churn.RoamMins
    ContractRenewal_yes = dict_churn.ContractRenewal_yes
    DataPlan_Yes = dict_churn.DataPlan_Yes

    sample = [AccountWeeks, DataUsage, CustServCalls,
            DayMins, DayCalls, MonthlyCharge,
            OverageFee, RoamMins, ContractRenewal_yes,
            DataPlan_Yes]

    np_sample = np.array(sample)

    prediction = LIGHT_GBM_CHURN.predict(np_sample.reshape(1, -1))

    return {"prediction": "churn" if prediction == 0 else "no-churn"}


@app.post("/prediction/churn_post_batch")
def pred_churn_post(Batch_churn: Batch_Value_Churn):
    dict_response = {}
    list_churn = Batch_churn.BatchValue

    for item in range(len(list_churn)):
        AccountWeeks = list_churn[item].AccountWeeks
        DataUsage = list_churn[item].DataUsage
        CustServCalls = list_churn[item].CustServCalls
        DayMins = list_churn[item].DayMins
        DayCalls = list_churn[item].DayCalls
        MonthlyCharge = list_churn[item].MonthlyCharge
        OverageFee = list_churn[item].OverageFee
        RoamMins = list_churn[item].RoamMins
        ContractRenewal_yes = list_churn[item].ContractRenewal_yes
        DataPlan_Yes = list_churn[item].DataPlan_Yes

        sample = [AccountWeeks, DataUsage, CustServCalls,
                DayMins, DayCalls, MonthlyCharge,
                OverageFee, RoamMins, ContractRenewal_yes,
                DataPlan_Yes]

        np_sample = np.array(sample)

        prediction = LIGHT_GBM_CHURN.predict(np_sample.reshape(1, -1))

        dict_response[f"sample_{item}"] = {"prediction": "churn" if prediction == 0 else "no-churn"}
 
    return dict_response

@app.get("/prediction/sentiment_analysis/transformer")
def sentiment_anaysis(message: str):
    from transformers import pipeline
    nlp = pipeline("sentiment-analysis")
    result = nlp(message)[0]

    return result