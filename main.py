from fastmcp import FastMCP
import random 
import json 


mcp=FastMCP("Simple calculator Server")

@mcp.tool
def add(a :int,b:int)->int:
    '''Adds the two given numbers
    Args : a-> first number
           b->second number 

    returns:
         The Sum of a and b

    '''
    return a+b

@mcp.tool
def random_number(min_val:int=1,max_val:int=100)->int:
    """ return a random nuymber between min_val and max_val"""
    return  random.randint(min_val,max_val)


@mcp.tool
def rool_dice()->int:
    """returns a number bertween 1 and 6"""
    return random.randint(1,6)

if __name__ == "__main__":
    mcp.run(transport="streamable-http",host="0.0.0.0",port=8000)
