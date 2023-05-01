import os
from flask import jsonify

from database import db
from db_models.images_model import ImagesModel
from web.images_api import images_blueprint


@images_blueprint.route('/convert-sketch-image', methods=['POST'])
def convert_sketch_image():
    """
    List Cars data
    This requests list all of car data
    """

    file = request.files['image']
    sketch_image = file.read()

    # create a new Image object with the file contents
    image = Image(data=file_contents)

    # add the image object to the database session and commit
    db.session.add(image)
    db.session.commit()

    # return a success response
    return 'Image uploaded successfully'


    from tasks.tasks import ImageGenerator

    cars_list = []
    generator = ImageGenerator('/home/talha927/Documents/jupyter/generator.h5')
    test_path = '/home/talha927/Documents/jupyter/images'
    test_images_path = [os.path.join(test_path, image_name) for image_name in os.listdir(test_path)]
    generator.generate_images(test_images_path, batch_size=5000)

    return jsonify(cars_list)


@images_blueprint.route('/converted-images-list', methods=['GET'])
def convert_sketch_image_():
    """
    List Cars data
    This requests list all of car data
    """
    cars_list = []
    # cars_data = db.session.query(CarModel).all()
    # for car in cars_data:
    #     cars_list.append(car.to_json())

    return jsonify(cars_list)
