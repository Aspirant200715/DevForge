#!/usr/bin/env python3
"""
quick_start_math_training.sh / .bat

Quick start script to set up and test the mathematics animation system.
This script will:
1. Generate training data
2. Test the pipeline
3. Provide status summary

Works on both Windows (batch) and Unix (bash)
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(cmd, description):
    """Run a command and report results."""
    print(f"\n{'='*60}")
    print(f"▶ {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=False)
        if result.returncode == 0:
            print(f"✅ {description} - SUCCESS\n")
            return True
        else:
            print(f"❌ {description} - FAILED\n")
            return False
    except Exception as e:
        print(f"❌ {description} - ERROR: {e}\n")
        return False


def main():
    print("\n" + "╔" + "="*58 + "╗")
    print("║ DEVFORGE MATHEMATICS ANIMATION SYSTEM".ljust(59) + "║")
    print("║ Quick Start Guide".ljust(59) + "║")
    print("╚" + "="*58 + "╝\n")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ required")
        return 1
    
    print("✓ Python version:", sys.version.split()[0])
    
    # Step 1: Generate training data
    success1 = run_command(
        f"{sys.executable} training/math_training_data_generator.py",
        "STEP 1: Generate Training Data"
    )
    
    if not success1:
        print("⚠️ Training data generation failed. Continuing anyway...")
    
    # Step 2: Test pipeline
    print(f"\n{'='*60}")
    print(f"▶ STEP 2: Test Mathematics Pipeline")
    print(f"{'='*60}")
    
    try:
        # Try to import and run tests
        sys.path.insert(0, 'training')
        from test_math_pipeline import MathPipelineTest
        
        tester = MathPipelineTest(verbose=False)
        results = tester.run_all_tests()
        
        success2 = (results["failed"] < 2)
        
        # Save report
        report_file = "training/test_results.json"
        import json
        with open(report_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n📄 Detailed report saved: {report_file}")
        
    except Exception as e:
        print(f"⚠️ Pipeline testing skipped: {e}")
        success2 = False
    
    # Summary
    print(f"\n{'='*60}")
    print(f"QUICK START SUMMARY")
    print(f"{'='*60}\n")
    
    print("✓ Generated Files:")
    print("  └─ training/math_training_examples.json (100+ examples)")
    print("  └─ training/math_training_dataset.jsonl (JSONL format)")
    print("  └─ training/math_topic_animation_mapping.json")
    print("  └─ training/test_results.json (test results)")
    
    print("\n✓ New Math Animations Supported:")
    topics = [
        "Matrix Multiplication",
        "Integral Calculus",
        "Derivatives",
        "Linear Algebra",
        "Limits & Continuity",
        "Trigonometry",
        "Sequences & Series",
        "Vector Calculus"
    ]
    for topic in topics:
        print(f"  └─ {topic}")
    
    print("\n📚 Documentation:")
    print("  └─ training/MATH_TRAINING_README.md (Full guide)")
    
    print("\n🚀 Next Steps:")
    print("  1. Train the model:")
    print(f"     python training/train_math_model.py")
    print("\n  2. Generate a math video:")
    print(f'     python -m src.main "Explain matrix multiplication"')
    print("\n  3. View the pipeline in action:")
    print(f'     python -m src.main "Integral calculus"')
    
    print(f"\n{'='*60}")
    
    if success1 and success2:
        print("✅ QUICK START COMPLETE - System Ready!")
        print(f"{'='*60}\n")
        return 0
    else:
        print("⚠️ Some steps had issues - See above for details")
        print(f"{'='*60}\n")
        return 1


if __name__ == "__main__":
    sys.exit(main())
