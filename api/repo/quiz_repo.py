class QuizRepo():
    def __init__(self, table):
        self.table = table
        
    async def get_quizzes(self):
        response = self.table.scan()
        return response["Items"]