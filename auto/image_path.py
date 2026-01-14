import os.path


def photo_auto(instance, name):
    auto = instance.auto
    make = auto.make.make.lower().replace(" ", "_")
    model_name = auto.model.lower().replace(" ", "_")
    body_name = auto.car_body.slug.lower().replace(" ", "_")
    full_name = f"{make}_{model_name}_{body_name}"

    return os.path.join("auto/", full_name, name)
