import project_1.body as body, project_1.holiday as holiday
import random

if __name__ == "__main__":
    m = random.choice([body, holiday])
    m.madlib()