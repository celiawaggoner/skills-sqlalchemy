"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.

id8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

models = Model.query.filter_by(name="Corvette", brand_name = "Chevrolet").all()

# Get all models that are older than 1960.

old_cars = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.

newer_brands = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

cor_models = Model.query.filter(Model.name.like("Cor%")).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.

brands = Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.

brands = Brand.query.filter(db.or_(Brand.discontinued.isnot(None), Brand.founded < 1950)).all()

# Get any model whose brand_name is not Chevrolet.

models = Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.filter(Model.year == year).all()

    output = ""

    for model in models:
        if model.brand:
            output += "%s, %s, %s \n" % (model.name, model.brand_name, model.brand.headquarters)

    print output


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = Brand.query.all()

    output = ""

    for brand in brands:
        output += brand.name + ": \n"
        for model in brand.models:
            output += "\t" + model.name + "\n"

    print output

#Discussion Question 1: Brand.query.filter_by(name='Ford') just returns
#the single query object and its location in the memory (I think?). 
#If I added .one() or .first() it would return a single object that matches 
#that query and if I added .all() it would return a list of objects.

#Discussion Question 2: An association table does not keep track of any other
#data, it just provides a link between two other tables and manages a 
#many to many relationship.

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    """Take in a string and return a list of brands whose name contains the string"""

    brands = Brand.query.filter(Brand.name.like('%' + mystr + '%')).all()

    return brands


def get_models_between(start_year, end_year):
    """Take in a start year and end year and return a list of models
    with years between the two dates"""

    models = Model.query.filter(Model.year > start_year, Model.year < end_year).all()

    return models 

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
