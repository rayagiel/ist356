# funcions
def clean_currency(value):
    '''
    This functions takes a value as a string and removes the $ and the comma. It returns a float value.
    '''
    value = value.replace(",","")
    value = value.replace("$","")
    float_value = float(value)
    return float_value

# this says if you are running the check_functions.py file this code will run, but if you are importing it into another file, it will not run
# it will only run the real functions and not the test code that is mainly for the person coding

def detect_whale(
        items_per_person:float, 
        price_per_person:float, 
        items_per_person_75th_pctile:float, 
        price_per_person_75_pctile:float) -> str:
    '''
    This function takes the items per person and price per person and along with the 75th percentile value for each.
    It returns a string indicating the type of customer. 
    '''
    if items_per_person > items_per_person_75th_pctile and price_per_person > price_per_person_75_pctile:
        return 'whale'
    if items_per_person > items_per_person_75th_pctile:
        return 'big eater'
    if price_per_person > price_per_person_75_pctile:
        return 'big spender'
    
    return 'normal'
if __name__ == "__main__":
    # test the clean_currencyfunction
    test_value = "$1,234.56"
    assert clean_currency("$1234.56") == 1234.56
    print("\nAll tests passed!")
