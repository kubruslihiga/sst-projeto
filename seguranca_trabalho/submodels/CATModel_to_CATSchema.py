from datetime import datetime
from ..schemas import CATSchema, CATBasicInfo, CATAccidentCommunication, Address, CATAccidentLocalization, CATAccidentLocalizationIdentification, CATBodyPartAffected, CATMedicalCertificate, CATDoctorInfo, CATSource
from .CAT import CATModel

def convert_to_schema(model: CATModel):
    ret = CATSchema()
    ret.accidentCommunication = convert_accident_communication(model)
    return ret

def convert_accident_communication(model: CATModel):
    ret = CATAccidentCommunication()
    if (model.accident_datetime):
        ret.date = model.accident_datetime.strftime("%d/%m/%y")
        ret.hour = model.accident_datetime.strftime("%H:%M")
    if (model.accident_type):
        ret.accidentType = model.accident_type.code
    if (model.cat_type):
        ret.catType = int(model.cat_type)
    if (model.accident_worked_hours):
        ret.workedHours = model.accident_worked_hours.strftime("%H:%M")
    if (model.accident_decease):
        ret.decease = model.accident_decease
    if (model.accident_decease_date):
        ret.deceaseDate = model.accident_decease_date.strftime("%d/%m/%y")
    if (model.accident_police_notification):
        ret.policeNotification = model.accident_police_notification
    if (model.accident_factor):
        ret.accidentFactor = model.accident_factor.code
    if (model.accident_communication_warning):
        ret.communicationWarning = int(model.accident_communication_warning)
    if (model.accident_notes):
        ret.notes = model.accident_notes
    return ret