import os, fire
from dotenv import load_dotenv
from src.runtime_client import LexRuntimeV2Client

load_dotenv(".env")
BOT_ID = os.environ.get("BOT_ID")
BOT_ALIAS_ID = os.environ.get("BOT_ALIAS_ID")

def test_successful_appointment_booking_intent():
    client = LexRuntimeV2Client(bot_id=BOT_ID, bot_alias_id=BOT_ALIAS_ID)
    assert client is not None
    assert isinstance(client, LexRuntimeV2Client)

    # Step 1
    response = client.recognize_text(text='Hola!', sessionState={})
    assert response is not None
    assert isinstance(response, dict)
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200
    
    sessionState = response['sessionState']
    assert sessionState is not None
    assert isinstance(sessionState, dict)
    assert sessionState['intent']['name'] == 'Greetings'

    messages = response['messages']
    assert messages is not None
    assert isinstance(messages, list)
    assert len(messages) != 0

    # Step 2
    response = client.recognize_text(text='Quiero reservar una cita', sessionState=sessionState)
    assert response is not None
    assert isinstance(response, dict)
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    sessionState = response['sessionState']
    assert sessionState is not None
    assert isinstance(sessionState, dict)
    assert sessionState['intent']['name'] == 'MakeAppointment'
    assert sessionState['intent']['state'] == 'InProgress'
    assert sessionState['intent']['confirmationState'] == 'None'

    messages = response['messages']
    assert messages is not None
    assert isinstance(messages, list)
    assert len(messages) != 0    

    # Step 3
    response = client.recognize_text(text='Quiero hacerme una limpieza', sessionState=sessionState)
    assert response is not None
    assert isinstance(response, dict)
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    sessionState = response['sessionState']
    assert sessionState is not None
    assert isinstance(sessionState, dict)
    assert sessionState['intent']['name'] == 'MakeAppointment'
    assert sessionState['intent']['slots']['AppointmentType']['value'] != {}
    assert sessionState['intent']['state'] == 'InProgress'
    assert sessionState['intent']['confirmationState'] == 'None'

    messages = response['messages']
    assert messages is not None
    assert isinstance(messages, list)
    assert len(messages) != 0    

    # Step 4
    response = client.recognize_text(text='A las 10 am', sessionState=sessionState)
    assert response is not None
    assert isinstance(response, dict)
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    sessionState = response['sessionState']
    assert sessionState is not None
    assert isinstance(sessionState, dict)
    assert sessionState['intent']['name'] == 'MakeAppointment'
    assert sessionState['intent']['slots']['Time']['value'] != {}
    assert sessionState['intent']['state'] == 'InProgress'
    assert sessionState['intent']['confirmationState'] == 'None'
    assert sessionState['dialogAction']['type'] == 'ConfirmIntent'

    messages = response['messages']
    assert messages is not None
    assert isinstance(messages, list)
    assert len(messages) != 0

    # Step 5
    response = client.recognize_text(text='Si', sessionState=sessionState)
    assert response is not None
    assert isinstance(response, dict)
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200

    sessionState = response['sessionState']
    assert sessionState is not None
    assert isinstance(sessionState, dict)
    assert sessionState['intent']['name'] == 'MakeAppointment'
    assert sessionState['intent']['state'] == 'Fulfilled'

    messages = response['messages']
    assert messages is not None
    assert isinstance(messages, list)
    assert len(messages) != 0    

    appointmentType = sessionState['intent']['slots']['AppointmentType']['value']['interpretedValue']
    time = sessionState['intent']['slots']['Time']['value']['interpretedValue']

    assert len(appointmentType) != 0
    assert len(time) != 0

