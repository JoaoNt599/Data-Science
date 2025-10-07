from fastapi import Request, HTTPException


async def validate_comment_body(request: Request):
    data = await request.json()
    comment = data.get("comment", "").strip()

    if not comment:
        raise HTTPException(status_code=400, detail="Comentário não pode ser vazio.")
    
    if comment.isnumeric():
        raise HTTPException(status_code=400, detail="Comentário não pode conter apenas números.")

    return data
