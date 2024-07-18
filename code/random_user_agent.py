import random

def random_user_agent():
    with open('code\\user_agent_list.txt', 'r', encoding='utf-8') as f:
        user_agents = f.readlines()
        return random.choice(user_agents).strip()
    
if __name__ == '__main__':
    print(random_user_agent())