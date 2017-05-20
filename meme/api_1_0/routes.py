from meme.api_1_0 import api_v1
from meme.api_1_0.resources.engineers import EngineerById, Engineers, EngineerTasksList
from meme.api_1_0.resources.tasks import TaskResource, TasksListResource, TasksFinishResource, TasksTimeResource

# GET /api/v1/engineers/<id> - returns engineer's data by it's id
api_v1.add_resource(EngineerById, '/engineers/<int:engineer_id>')

# GET /api/v1/engineers - returns list of all engineers
# POST { "full_name" : "John Smith Jr." } /api/v1/engineers - creates engineer
api_v1.add_resource(Engineers, '/engineers')

# GET /api/v1/engineers/<int:engineer_id>/tasks - returns list of all tasks assigned to engineer
api_v1.add_resource(EngineerTasksList, '/engineers/<int:engineer_id>/tasks')



api_v1.add_resource(TaskResource, '/tasks/<int:task_id>')
api_v1.add_resource(TasksListResource, '/tasks')
api_v1.add_resource(TasksFinishResource, '/tasks/<int:task_id>/finish')
api_v1.add_resource(TasksTimeResource, '/tasks/period')
