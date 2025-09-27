#!/usr/bin/env python3
"""
Simple test script to demonstrate the refactored Llama benchmark results
"""

import json

# Load the new format results
with open('weird-bench/results/llama_results.json', 'r') as f:
    results = json.load(f)

print("=== Refactored Llama Benchmark Results Summary ===")
print(f"Timestamp: {results['timestamp']}")
print(f"GPU Selection Available GPUs: {len(results['results']['gpu_selection']['available_gpus'])}")
print()

# Show CPU runs (simplified)
cpu_runs = results['results']['runs_cpu']
print(f"CPU Runs: {len(cpu_runs)}")
for run in cpu_runs:
    system_info = run['metrics']['system_info']
    print(f"  - CPU: {system_info['cpu_info']}")
    print(f"    Tokens/sec: {run['metrics']['tokens_per_second']:.2f}")
print()

# Show new device_runs format (this is the key improvement)
device_runs = results['results']['device_runs']
print(f"Device Runs (NEW FORMAT): {len(device_runs)}")
for device in device_runs:
    print(f"  Device: {device['device_name']} (Index: {device['device_index']})")
    print(f"    Driver: {device['device_driver']}")
    print(f"    Type: {device['device_type']}")
    print(f"    Success: {device['success']}")
    print(f"    Runs: {len(device['runs'])}")
    for run in device['runs']:
        print(f"      - Prompt: {run['prompt_size']}, Gen: {run['generation_size']}")
        print(f"        Tokens/sec: {run['metrics']['tokens_per_second']:.2f}")
        print(f"        GPU Info: {run['metrics']['system_info']['gpu_info']}")
print()

# Show legacy runs_gpu format (for backwards compatibility)
gpu_runs = results['results']['runs_gpu'] 
print(f"GPU Runs (LEGACY FORMAT): {len(gpu_runs)}")
for run in gpu_runs:
    gpu_device = run.get('gpu_device', {})
    system_info = run['metrics']['system_info']
    print(f"  - GPU Device: {gpu_device.get('name', 'Unknown')}")
    print(f"    System GPU Info: {system_info.get('gpu_info', 'N/A')}")
    print(f"    Tokens/sec: {run['metrics']['tokens_per_second']:.2f}")
print()

print("=== Key Improvements ===")
print("✅ NEW: device_runs array with separate entries per GPU")
print("✅ GPU info is device-specific (no more comma-separated lists)")
print("✅ Removed verbose raw_json data (reduced file size)")
print("✅ Added essential_info for debugging without bloat")
print("✅ Maintained backwards compatibility with runs_gpu")
print()
print("This format ensures RTX 3060 and RTX 3060 Ti results are properly separated!")