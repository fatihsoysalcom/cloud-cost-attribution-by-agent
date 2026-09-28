import collections

# --- Configuration: Define cost rates for different resource types ---
# This simulates how different cloud services might have different pricing.
COST_RATES = {
    "compute_unit": 0.05,  # Cost per compute unit
    "storage_gb": 0.01,    # Cost per GB of storage
    "network_gb": 0.02,    # Cost per GB of network transfer
}

# --- Simulated Cost Events: Data representing resource usage ---
# Each entry represents a specific resource usage event,
# crucially tagged with an 'agent' (e.g., project, team, user).
# This 'agent' tag is the key for granular cost attribution.
cost_events = [
    # Project Alpha events
    {"agent": "Project Alpha", "resource_type": "compute_unit", "units_consumed": 100},
    {"agent": "Project Alpha", "resource_type": "storage_gb", "units_consumed": 50},
    {"agent": "Project Alpha", "resource_type": "network_gb", "units_consumed": 20},
    {"agent": "Project Alpha", "resource_type": "compute_unit", "units_consumed": 150},

    # Project Beta events
    {"agent": "Project Beta", "resource_type": "compute_unit", "units_consumed": 200},
    {"agent": "Project Beta", "resource_type": "storage_gb", "units_consumed": 100},
    {"agent": "Project Beta", "resource_type": "network_gb", "units_consumed": 30},

    # Project Gamma events (e.g., a new project or a smaller one)
    {"agent": "Project Gamma", "resource_type": "compute_unit", "units_consumed": 50},
    {"agent": "Project Gamma", "resource_type": "storage_gb", "units_consumed": 20},

    # Another event for Project Alpha
    {"agent": "Project Alpha", "resource_type": "storage_gb", "units_consumed": 30},
]

# --- Cost Attribution Logic ---
# This is where we aggregate costs based on the 'agent' tag.
# Traditional dashboards often miss this step, showing only total costs.
agent_costs = collections.defaultdict(float) # Use defaultdict for easy aggregation

print("--- Processing Cost Events ---")
for i, event in enumerate(cost_events):
    agent = event["agent"]
    resource_type = event["resource_type"]
    units = event["units_consumed"]

    if resource_type in COST_RATES:
        cost = units * COST_RATES[resource_type]
        agent_costs[agent] += cost # Attributing cost to the specific agent
        print(f"  Event {i+1}: {agent} used {units} {resource_type} -> Cost: ${cost:.2f}")
    else:
        print(f"  Warning: Unknown resource type '{resource_type}' for {agent}. Skipping.")

print("\n--- Cost Breakdown by Agent ---")
total_cost = 0.0
for agent, cost in sorted(agent_costs.items()):
    print(f"  {agent}: ${cost:.2f}")
    total_cost += cost

print(f"\nTotal Simulated Cost: ${total_cost:.2f}")

# --- Demonstration of the problem addressed by the article ---
print("\n--- What a traditional dashboard might show (without agent breakdown) ---")
print(f"Total Cloud Spend: ${total_cost:.2f}")
# This output highlights the article's point: without agent-based tracking,
# you only see the total, not who is responsible for which part.
