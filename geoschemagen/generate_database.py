import numpy as np
from geoschemagen.create_schema import create_schema, create_schema_noRF, create_schema_eight_layers, create_schema_eight_layers_noRF


def generate_database(output_folder: str, no_realizations: int, z_max: int, x_max: int, seed:int, no_layers:int = 5, use_RF:bool = True):
    """
    Generate a database of synthetic data with given parameters and save results in the specified output folder.

    Args:
        output_folder (str): The folder to save the synthetic data.
        no_realizations (int): The number of realizations to generate.
        z_max (int): The depth of the model.
        x_max (int): The length of the model.
        seed (int): The seed for the random number generator.
        no_layers (int): The number of layers in the model. Default is 5.
        use_RF (bool): Whether to use Random Fields. Default is True.

    Return:
        None
    """
    # Set the seed for NumPy's random number generator
    np.random.seed(seed)

    # Start the counter
    counter = 0
    # Loop through the number of realizations
    while counter < no_realizations:
        try:
            # Print the realization number
            print('Generating model no.:', counter+1)
            # Check if the user wants to use Random Fields
            if use_RF == True:
                if no_layers == 5:
                    create_schema(output_folder, counter, z_max, x_max, seed)
                elif no_layers == 8:
                    create_schema_eight_layers(output_folder, counter, z_max, x_max, seed)
                else:
                    print("Number of layers not supported")

            elif use_RF == False:
                if no_layers == 5:
                    create_schema_noRF(output_folder, counter, z_max, x_max, seed)
                elif no_layers == 8:
                    create_schema_eight_layers_noRF(output_folder, counter, z_max, x_max, seed)
                else:
                    print("Number of layers not supported")
            # Increment the counter
            counter += 1

        # Catch any exceptions and print the error
        except Exception as e:
            print(f"Error in generating model no. {counter + 1}: {e}")
            continue