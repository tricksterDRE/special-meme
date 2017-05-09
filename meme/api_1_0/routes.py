from meme.api_1_0 import api_v1
from meme.api_1_0.resources.engineers import EngineersResource
from meme.api_1_0.resources.engineers import EngineersListResource

api_v1.add_resource(EngineersResource, '/engineers/<int:engineer_id>')
api_v1.add_resource(EngineersListResource, '/engineers')
