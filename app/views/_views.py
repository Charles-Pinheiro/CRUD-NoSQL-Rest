from flask import Flask, request
from flask.json import jsonify
from app.models.post_model import Post


def init_app(app: Flask):

    @app.route('/posts', methods=['POST'])
    def create_post():
        data = request.json

        try:
            post = Post(**data)
            post.create_id()
            created = post.create_post()
            if created:
                return {'message': 'Conteúdo publicado!'}, 201
        except TypeError:
            return {'message': 'Envie todos os dados necessários.'}, 400


    @app.route('/posts/<int:id>', methods=['DELETE'])
    def delete_post(id):
        try:
            Post.get_by_id(id)
            Post.delete_post(id)
            return {'message': 'Postagem excluída'}, 200
        except TypeError:
            return {'message': 'Essa publicação não existe.'}, 400


    @app.route('/posts/<int:id>', methods=['GET'])
    def read_post_by_id(id):
        try:
            return Post.get_by_id(id)
        except TypeError:
            return {'message': 'Essa publicação não existe.'}, 400


    @app.route('/posts', methods=['GET'])
    def read_posts():
        posts_list = Post.get_all()
        return jsonify(posts_list), 200


    @app.route('/posts/<int:id>', methods=['PATCH'])
    def update_post(id):
        data = request.json
        try:
            Post.get_by_id(id)
            Post.update_post(data, id)
            return Post.get_by_id(id), 200
        except TypeError:
            return {'message': 'Essa publicação não existe.'}, 400
