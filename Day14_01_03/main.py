from agent import Agent, Boss

# =====================================================
# MAIN PROGRAM USAGE
# =====================================================

# Creating normal agent
p1 = Agent("Sam", 27)

print(p1.info())

p1.current_health()

p1.punched()
p1.current_health()

p1.shot()
p1.current_health()

print("Alive?", p1.is_alive())

p1.shot()
p1.current_health()

print("Alive?", p1.is_alive())
print(p1.info())


# Custom health
p_custom = Agent("Custom", 30, health=250)
print(p_custom.info())


# Creating Boss object
b1 = Boss("Hardik", 200)

print(b1.info())      # Inherited method
b1.blow_fire()        # Boss-specific method
b1.punched()          # Inherited method
print(b1.info())


print(dir(Agent))