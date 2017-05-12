from meme.api_1_0 import api_v1
from meme.api_1_0.resources.engineers import EngineerResource, EngineersListResource, EngineersTasksResource
from meme.api_1_0.resources.tasks import TaskResource, TasksListResource, TasksFinishResource, TasksTimeResource

api_v1.add_resource(EngineerResource, '/engineers/<int:engineer_id>')
api_v1.add_resource(EngineersListResource, '/engineers')
api_v1.add_resource(EngineersTasksResource, '/engineers/<int:engineer_id>/tasks')

api_v1.add_resource(TaskResource, '/tasks/<int:task_id>')
api_v1.add_resource(TasksListResource, '/tasks')
api_v1.add_resource(TasksFinishResource, '/tasks/<int:task_id>/finish')
api_v1.add_resource(TasksTimeResource, '/tasks/period')
