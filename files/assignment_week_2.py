#Assignment week 2 Git and repo management 
#In this assignment, you will practice creating and managing branches, 
# committing and pushing changes, resolving a merge conflict, 
# and deleting a branch after it has been merged.

#Step 1: Fork this repo to your own GitHub account.

#Step 2: Open this repository on your chosen IDE 

#Step 2: Create a new branch called "milk_yield_conversion"

    # Make sure to switch to the new branch before making any changes.
    #In this branch we will implement the milk yield conversion function.

#Step 3: Change the following function so it converts milk yield from pounds to kilograms.
#Include documentation with your written function in the functions docstring. 
# safe the file

#base function 
def convert_milk_yield_kg_to_lbs(value):
    """
    Convert milk yield from kilograms to pounds.

    Args:
        value (float): Milk yield in kilograms.

    Returns:
        float: Milk yield converted to pounds using the conversion
        factor 1 kilogram = 2.20462 pounds.
    """
    return value * 2.20462
 
#base function 
def convert_milk_yield_lbs_to_kg(value):
    """
    Convert milk yield from pounds to kilograms.

    Args:
        value (float): Milk yield in pounds.

    Returns:
        float: Milk yield converted to kilograms using the conversion
        factor 1 pound = 0.45359237 kilograms.
    """
    return value * 0.45359237

#Step 4: Commit your changes to the new branch and push it to the remote repository. 
# Make sure each step to push to your fork and not the original repo.

#Step 5: Switch back to the main branch, but do not merge the changes from the "milk_yield_conversion" branch yet! 

#Step 6: On the main branch, create a new function also called "convert_milk_yield" that converts milk yield from kilograms to pounds.
# Save your change. 

#Step 7: Commit your changes to the main branch and push it to the remote repository.

#Step 8: Try to merge the "milk_yield_conversion" branch into the main branch. 

#Step 9: Resolve any merge conflicts that arise during the merge process by keeping only the changes from main. 

#Step 10: Go back to the milk_conversion_branch.
# Instead of changing the function make a new function called "convert_milk_yield_kg_to_lbs"
# safe changes and commit the changes to the milk_conversion_branch.

#Step 11: Switch back to the main branch and merge the "milk_yield_conversion" branch into the main branch.
# Push the changes to the remote repository and verify that the merge was successful by checking the main branch for both functions.

#Step 12: Submit the link to your forked repository on GitHub for review on Canvas. 





