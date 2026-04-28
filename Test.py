# 1. Define a simple Tool class
class Tool:
    def __init__(self, name, description):
        self.name = name
        self.description = description

# 2. Create a list of tool objects
tools = [
    Tool("sql_query", "Runs a query against the sales database"),
    Tool("web_search", "Searches the internet for real-time data"),
    Tool("calculator", "Performs math operations")
]

# 3. Apply the line of code
tools_dict = {tool.name: tool for tool in tools}
print(tools_dict)

# 4. Resulting dictionary looks like this:
# {
#   "sql_query": <Tool object at 0x...>,
#   "web_search": <Tool object at 0x...>,
#   "calculator": <Tool object at 0x...>
# }

# 5. Why do this? Fast Lookup!
# Instead of looping through the list to find the SQL tool, you just do:
my_tool = tools_dict["web_search"]
print(my_tool.description) 
# Output: Runs a query against the sales database