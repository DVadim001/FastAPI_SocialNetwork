from pydantic import BaseModel


class PublicPostValidator(BaseModel):
    post_id: int
    comment_text: str
    user_id: int


class EditPostValidator(BaseModel):
    post_id: int
    comment_id: int
    change_text: str
