import pytest
from sqlalchemy import insert
from web.database import db_session
from web.models.pages import Pages

@pytest.fixture(params=['spongebob', 'spongebob_blog'])
def setup_spongebob_pages(request):
    stmt = (insert(Pages).values(name=request.param))
    db_session.execute(stmt)
    return request.param_index + 1
