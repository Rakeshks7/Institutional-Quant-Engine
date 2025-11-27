import numpy as np
import random

class TradingAgent:
    def __init__(self, action_size=3):
        self.action_size = action_size 
        self.q_table = {} 
        self.learning_rate = 0.1
        self.discount_factor = 0.95
        self.epsilon = 1.0 

    def get_state(self, price, avg_price):
        return "ABOVE" if price > avg_price else "BELOW"

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size) 
        if state not in self.q_table:
            return 0 
        return np.argmax(self.q_table[state]) 

    def learn(self, state, action, reward, next_state):
        current_q = self.q_table.get((state, action), 0.0)
        max_future_q = np.max(self.q_table.get(next_state, [0, 0, 0])) if next_state in self.q_table else 0
        
        new_q = (1 - self.learning_rate) * current_q + self.learning_rate * (reward + self.discount_factor * max_future_q)
        
        if state not in self.q_table: self.q_table[state] = [0, 0, 0]
        self.q_table[state][action] = new_q

agent = TradingAgent()
prices = [100, 102, 105, 103, 98, 95, 99, 105] 
avg = 100

print("🤖 AGENT TRAINING LOG:")
for i in range(len(prices)-1):
    current_price = prices[i]
    next_price = prices[i+1]
    
    state = agent.get_state(current_price, avg)
    action = agent.act(state) 
    
    reward = 0
    if action == 1: 
        reward = next_price - current_price
    elif action == 2: 
        reward = current_price - next_price
        
    next_state = agent.get_state(next_price, avg)
    agent.learn(state, action, reward, next_state)
    
    action_name = ["HOLD", "BUY", "SELL"][action]
    print(f"Step {i}: Price {current_price} -> Action: {action_name} -> Reward: {reward}")