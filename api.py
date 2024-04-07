from vetiver import VetiverModel
from vetiver import VetiverAPI
import pins

b = pins.board_folder('data/model', allow_pickle_read=True)

v = VetiverModel.from_pin(b, 'penguin_model')

app = VetiverAPI(v, check_prototype=True)

app.run(port = 8080)
