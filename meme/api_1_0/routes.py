from meme.api_1_0 import api_v1

from meme.api_1_0.resources.engineers import Engineers
from meme.api_1_0.resources.engineer_tasks import EngineerTasks

from meme.api_1_0.resources.tasks import Tasks
from meme.api_1_0.resources.tasks_finalizer import TasksFinalizer
from meme.api_1_0.resources.tasks_in_period import TasksInPeriod

# GET /api/v1/engineers - returns list of all engineers
# POST
# {
#   "full_name" : "John Smith Jr."
# }
# /api/v1/engineers - creates engineer
api_v1.add_resource(Engineers, '/engineers')

# GET /api/v1/engineers/<id>/tasks - returns list of all tasks assigned to engineer
api_v1.add_resource(EngineerTasks, '/engineers/<int:engineer_id>/tasks')

# GET /api/v1/tasks - return all tasks
# POST
# {
#   "id_engineer": 41,
#   "task_name": "Укусить мангуста",
#   "task_description": "Мангуст стал слишком борзым. Пришло время показать ему, кто здесь главный",
#   "start_time": "22.03.2017 15:00:47",
#   "photo_required": true
# }
# /api/v1/tasks - creates task
api_v1.add_resource(Tasks, '/tasks')

# POST
# {
#   "comment": "Я укусил! Я укусил мангуста!.. Я догнал! Я укусил! Я догнал и укусил мангуста!!!1",
#   "end_time": "01.11.2018 05:10:01",
#   "gps_longitude": 100.200,
#   "gps_latitude": 200.300,
#   "link": "https://ds03.infourok.ru/uploads/ex/05f2/00054999-d4e4ca05/640/img43.jpg"
# }
# /api/v1/tasks/<id>/finish
api_v1.add_resource(TasksFinalizer, '/tasks/<int:task_id>/finish')

# G
# {
#   "period_start": "21.03.2017 00:00:00",
#   "period_end": "23.03.2017 00:00:00"
# }
# /api/v1/tasks/period
api_v1.add_resource(TasksInPeriod, '/tasks/period')
