class Tree:
    def __init__(self, root):
        self.root = root 
    def get_element_by_id(self, target_id):
        def dfs(node):
         
            if node['id'] == target_id:
                return node

            for child in node['children']:
                result = dfs(child)
                if result:
                    return result
            
            return None  
       
        return dfs(self.root)
