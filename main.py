from functools import wraps

from flask import Flask, g, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Configuração do Swagger UI
SWAGGER_URL = "/docs"
API_URL = "/static/swagger.yml"
SWAGGER_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "To-do API"},
)

app.register_blueprint(SWAGGER_BLUEPRINT, url_prefix=SWAGGER_URL)

admins: dict[str, bool] = {
    "Murilo": True,
    "Nicola": True,
    "Muricola": True,
    "Andre": True,
}

tasks: dict[str, list[dict[str, str]]] = {}


def auth(f):
    @wraps(f)
    def auth_function(*args, **kwargs):
        try:
            user = request.headers.get("Authorization")

            if user is None:
                raise KeyError("No auth provided")

            verify = tasks.get(user)

            if verify is None or verify == False:
                raise KeyError("User not authorized")

            g.user = user
            return f(*args, **kwargs)

        except Exception as err:
            return jsonify({"message": f"{err}"}), 401

    return auth_function


def admin_auth(f):
    @wraps(f)
    def admin_auth_function(*args, **kwargs):
        try:
            user = request.headers.get("Authorization")

            if user is None:
                raise KeyError("No auth provided")

            verify = admins.get(user)

            if verify is None or verify == False:
                raise KeyError("User not authorized")

            g.user = user
            return f(*args, **kwargs)

        except Exception as err:
            return jsonify({"message": f"{err}"}), 401

    return admin_auth_function


@app.post("/create_user")
@admin_auth
def create_user_route():
    if request.is_json:
        data = request.get_json()

        user_name = data.get("user_name")

        if user_name is None or type(user_name) != str:
            return jsonify(message="No user_name provided"), 400

        tasks[user_name] = []

        return jsonify(message="User created with success!"), 201
    else:
        return jsonify(message="The request body must be a json"), 400


@app.post("/create_task")
@auth
def create_task_route():
    if request.is_json:
        user_name = getattr(g, "user", None)

        if user_name is None:
            return jsonify(message="Auth didn't provided user"), 404

        data = request.get_json()

        to_do_task = data.get("task")

        if to_do_task is None or type(to_do_task) != str:
            return jsonify(message="No user_name provided"), 400

        this_user_tasks = tasks.get(user_name)

        if this_user_tasks is None:
            return jsonify(message="Create user firts"), 500

        task_to_add = {
            "id": len(this_user_tasks) + 1,
            "task": to_do_task,
            "status": "pending",
        }

        tasks[user_name].append(task_to_add)

        return jsonify(message="Task created with success"), 201

    else:
        return jsonify(message="The request body must be a json"), 400


@app.get("/tasks")
@auth
def get_all_tasks_routes():
    user_name = getattr(g, "user", None)

    if user_name is None:
        return jsonify(message="Auth didn't provided user"), 404

    this_tasks = tasks.get(user_name)

    if this_tasks is None:
        return jsonify(message="This user doesn't have any task"), 500

    return jsonify(tasks=this_tasks), 200


@app.put("/update_task")
@auth
def update_task_route():
    if request.is_json:
        user_name = getattr(g, "user", None)

        if user_name is None:
            return jsonify(message="Auth didn't provided user"), 404

        data = request.get_json()

        task_id = data.get("task_id")
        new_task_status = data.get("status")
        modified = False

        if new_task_status is None or type(new_task_status) != str or task_id is None:
            return jsonify(message="Uncomplited body"), 400

        this_user_tasks = tasks.get(user_name)

        if this_user_tasks is None:
            return jsonify(message="Create user firts"), 500

        for task in this_user_tasks:
            if task["id"] == task_id:
                task["status"] = new_task_status
                modified = True

        if modified == True:
            return jsonify(message="Task modified with success"), 202

        return jsonify(message="Task doesn't exists"), 500

    else:
        return jsonify(message="The request body must be a json"), 400


@app.delete("/delete_task")
@auth
def delete_task_route():
    if request.is_json:
        user_name = getattr(g, "user", None)

        if user_name is None:
            return jsonify(message="Auth didn't provided user"), 404

        data = request.get_json()

        task_id = data.get("task_id")
        modified = False

        if task_id is None:
            return jsonify(message="Uncomplited body"), 400

        this_user_tasks = tasks.get(user_name)

        if this_user_tasks is None:
            return jsonify(message="Create user firts"), 500

        for i, task in enumerate(this_user_tasks):
            if task["id"] == task_id:
                del this_user_tasks[i]
                modified = True

        if modified == True:
            return jsonify(message="Task deleted with success"), 203

        return jsonify(message="Task doesn't exists"), 500

    else:
        return jsonify(message="The request body must be a json"), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, threaded=False)
