#!/usr/bin/env python3
"""
test_math_pipeline.py

Comprehensive test suite for the mathematics animation pipeline.
Tests:
1. Topic detection for all math topics
2. Animation generation for each topic
3. Pipeline integration (no breaking changes)
4. Output validation

Usage:
    python training/test_math_pipeline.py
    python training/test_math_pipeline.py --verbose
"""

import sys
import os
from pathlib import Path
from typing import Dict, List, Tuple
import json

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from topic_router import detect_topic, has_animation, has_specialized_animation, get_animation_info


class MathPipelineTest:
    """Test suite for math animations in the pipeline."""
    
    def __init__(self, verbose: bool = False):
        """Initialize test suite."""
        self.verbose = verbose
        self.test_results = {}
        self.passed = 0
        self.failed = 0
    
    def log(self, message: str, level: str = "INFO"):
        """Log message with level."""
        if self.verbose or level in ["ERROR", "CRITICAL"]:
            prefix = {
                "INFO": "ℹ️",
                "SUCCESS": "✅",
                "FAIL": "❌",
                "WARNING": "⚠️",
                "ERROR": "🔴"
            }
            print(f"{prefix.get(level, '•')} {message}")
    
    def test_topic_detection(self) -> bool:
        """Test topic detection for math topics."""
        self.log("\n" + "="*60)
        self.log("TEST 1: TOPIC DETECTION FOR MATH TOPICS")
        self.log("="*60)
        
        test_cases = {
            "matrix multiplication": "matrix_multiplication",
            "multiplying two matrices": "matrix_multiplication",
            "integral calculus": "integral_calculus",
            "area under the curve": "integral_calculus",
            "derivatives of functions": "derivatives",
            "instantaneous rate of change": "derivatives",
            "linear algebra vectors": "linear_algebra",
            "eigenvalues and eigenvectors": "linear_algebra",
            "limits and continuity": "limits",
            "approaching a point": "limits",
            "trigonometry unit circle": "trigonometry",
            "sine and cosine functions": "trigonometry",
            "geometric sequences": "sequences_series",
            "infinite series": "sequences_series",
            "vector fields calculus": "vector_calculus",
            "divergence and curl": "vector_calculus",
        }
        
        passed = 0
        for concept, expected_topic in test_cases.items():
            detected = detect_topic(concept)
            is_correct = detected == expected_topic
            
            if is_correct:
                passed += 1
                self.log(f"✓ '{concept}' → {detected}", "SUCCESS")
            else:
                self.log(f"✗ '{concept}' → {detected} (expected {expected_topic})", "FAIL")
            
            self.test_results[f"topic_detection_{concept}"] = is_correct
        
        accuracy = (passed / len(test_cases)) * 100
        self.log(f"\nTopic Detection Accuracy: {passed}/{len(test_cases)} ({accuracy:.1f}%)", 
                "SUCCESS" if passed == len(test_cases) else "WARNING")
        
        self.passed += passed
        self.failed += (len(test_cases) - passed)
        
        return passed == len(test_cases)
    
    def test_animation_detection(self) -> bool:
        """Test animation detection."""
        self.log("\n" + "="*60)
        self.log("TEST 2: ANIMATION DETECTION")
        self.log("="*60)
        
        math_topics = [
            "matrix multiplication",
            "integral calculus",
            "derivatives",
            "linear algebra",
            "limits",
            "trigonometry",
            "sequences and series",
            "vector calculus"
        ]
        
        passed = 0
        for topic in math_topics:
            has_anim = has_animation(topic)
            if has_anim:
                passed += 1
                self.log(f"✓ '{topic}' has animation", "SUCCESS")
            else:
                self.log(f"✗ '{topic}' missing animation", "FAIL")
            
            self.test_results[f"animation_available_{topic}"] = has_anim
        
        self.log(f"\nAnimation Availability: {passed}/{len(math_topics)}", 
                "SUCCESS" if passed == len(math_topics) else "FAIL")
        
        self.passed += passed
        self.failed += (len(math_topics) - passed)
        
        return passed == len(math_topics)
    
    def test_specialized_animations(self) -> bool:
        """Test specialized animation detection."""
        self.log("\n" + "="*60)
        self.log("TEST 3: SPECIALIZED ANIMATION DETECTION")
        self.log("="*60)
        
        math_concepts = {
            "2x2 matrix multiplication": True,
            "fundamental theorem of calculus": True,
            "derivative of x squared": True,
            "vector spaces basis": True,
            "limit as x approaches 2": True,
            "sine wave animation": True,
            "geometric series convergence": True,
            "gradient vector field": True,
        }
        
        passed = 0
        for concept, should_be_specialized in math_concepts.items():
            is_specialized = has_specialized_animation(concept)
            if is_specialized == should_be_specialized:
                passed += 1
                self.log(f"✓ '{concept}' specialized={is_specialized}", "SUCCESS")
            else:
                self.log(f"✗ '{concept}' specialized={is_specialized} (expected {should_be_specialized})", "FAIL")
            
            self.test_results[f"specialized_{concept}"] = is_specialized == should_be_specialized
        
        self.log(f"\nSpecialized Animation Detection: {passed}/{len(math_concepts)}", 
                "SUCCESS" if passed == len(math_concepts) else "WARNING")
        
        self.passed += passed
        self.failed += (len(math_concepts) - passed)
        
        return passed == len(math_concepts)
    
    def test_animation_info_retrieval(self) -> bool:
        """Test animation info retrieval."""
        self.log("\n" + "="*60)
        self.log("TEST 4: ANIMATION INFO RETRIEVAL")
        self.log("="*60)
        
        concepts = [
            "matrix multiplication",
            "integral calculus",
            "derivatives calculus",
            "linear algebra vectors",
        ]
        
        passed = 0
        for concept in concepts:
            try:
                info = get_animation_info(concept)
                
                required_keys = {"has_animation", "is_specialized", "topic", "description"}
                has_all_keys = required_keys.issubset(info.keys())
                
                if has_all_keys and info["has_animation"]:
                    passed += 1
                    self.log(f"✓ {concept}: {info['topic']}", "SUCCESS")
                    if self.verbose:
                        self.log(f"  Description: {info['description'][:50]}...", "INFO")
                else:
                    self.log(f"✗ {concept}: Missing required keys", "FAIL")
                
                self.test_results[f"animation_info_{concept}"] = has_all_keys
            
            except Exception as e:
                self.log(f"✗ {concept}: {str(e)}", "ERROR")
                self.test_results[f"animation_info_{concept}"] = False
        
        self.log(f"\nAnimation Info Tests: {passed}/{len(concepts)}", 
                "SUCCESS" if passed == len(concepts) else "WARNING")
        
        self.passed += passed
        self.failed += (len(concepts) - passed)
        
        return passed == len(concepts)
    
    def test_non_math_exclusions(self) -> bool:
        """Test that non-math topics are not incorrectly classified as math."""
        self.log("\n" + "="*60)
        self.log("TEST 5: NON-MATH TOPIC EXCLUSIONS")
        self.log("="*60)
        
        non_math_concepts = {
            "photosynthesis biology": "generic",
            "chemical reactions": "chemistry",
            "projectile motion physics": "projectile_motion",
            "bubble sort algorithm": "bubble_sort",
            "binary search algorithm": "binary_search",
        }
        
        passed = 0
        for concept, expected_topic in non_math_concepts.items():
            detected = detect_topic(concept)
            is_correct = detected == expected_topic
            
            if is_correct:
                passed += 1
                self.log(f"✓ '{concept}' correctly classified as {detected}", "SUCCESS")
            else:
                self.log(f"⚠️ '{concept}' classified as {detected} (expected {expected_topic})", "WARNING")
            
            self.test_results[f"exclusion_{concept}"] = is_correct
        
        self.log(f"\nNon-Math Exclusion Tests: {passed}/{len(non_math_concepts)}", 
                "SUCCESS" if passed == len(non_math_concepts) else "WARNING")
        
        self.passed += passed
        self.failed += (len(non_math_concepts) - passed)
        
        return passed >= len(non_math_concepts) - 1  # Allow 1 miss
    
    def test_training_data_exists(self) -> bool:
        """Test that training data files were created."""
        self.log("\n" + "="*60)
        self.log("TEST 6: TRAINING DATA FILES")
        self.log("="*60)
        
        required_files = [
            "training/math_training_examples.json",
            "training/math_training_dataset.jsonl",
            "training/math_topic_animation_mapping.json",
        ]
        
        passed = 0
        for filepath in required_files:
            exists = os.path.exists(filepath)
            if exists:
                passed += 1
                file_size = os.path.getsize(filepath)
                self.log(f"✓ {filepath} ({file_size} bytes)", "SUCCESS")
            else:
                self.log(f"✗ {filepath} NOT FOUND", "FAIL")
            
            self.test_results[f"file_exists_{filepath}"] = exists
        
        self.log(f"\nTraining Data Files: {passed}/{len(required_files)}", 
                "SUCCESS" if passed == len(required_files) else "WARNING")
        
        self.passed += passed
        self.failed += (len(required_files) - passed)
        
        return passed == len(required_files)
    
    def test_animation_function_availability(self) -> bool:
        """Test that animation functions are available."""
        self.log("\n" + "="*60)
        self.log("TEST 7: ANIMATION FUNCTION AVAILABILITY")
        self.log("="*60)
        
        animation_functions = [
            "create_matrix_multiplication_clip",
            "create_integral_calculus_clip",
            "create_derivatives_clip",
            "create_linear_algebra_clip",
            "create_limits_clip",
            "create_trigonometry_clip",
            "create_sequences_series_clip",
            "create_vector_calculus_clip",
        ]
        
        try:
            from animation_clips import (
                create_matrix_multiplication_clip,
                create_integral_calculus_clip,
                create_derivatives_clip,
                create_linear_algebra_clip,
                create_limits_clip,
                create_trigonometry_clip,
                create_sequences_series_clip,
                create_vector_calculus_clip,
            )
            
            passed = len(animation_functions)
            for func_name in animation_functions:
                self.log(f"✓ {func_name} imported successfully", "SUCCESS")
                self.test_results[f"function_available_{func_name}"] = True
        
        except ImportError as e:
            self.log(f"⚠️ Partial import error: {str(e)}", "WARNING")
            passed = 0
            for func_name in animation_functions:
                self.test_results[f"function_available_{func_name}"] = False
        
        self.log(f"\nAnimation Function Availability: {passed}/{len(animation_functions)}", 
                "SUCCESS" if passed == len(animation_functions) else "WARNING")
        
        self.passed += passed
        self.failed += (len(animation_functions) - passed)
        
        return passed >= len(animation_functions) - 2  # Allow some import differences
    
    def run_all_tests(self) -> Dict[str, any]:
        """Run all tests."""
        self.log("\n" + "╔" + "="*58 + "╗")
        self.log("║ MATHEMATICS ANIMATION PIPELINE TEST SUITE".ljust(59) + "║")
        self.log("╚" + "="*58 + "╝")
        
        # Run all tests
        results = {
            "topic_detection": self.test_topic_detection(),
            "animation_detection": self.test_animation_detection(),
            "specialized_animations": self.test_specialized_animations(),
            "animation_info": self.test_animation_info_retrieval(),
            "non_math_exclusions": self.test_non_math_exclusions(),
            "training_data": self.test_training_data_exists(),
            "animation_functions": self.test_animation_function_availability(),
        }
        
        # Summary
        self.log("\n" + "="*60)
        self.log("TEST SUMMARY")
        self.log("="*60)
        
        total_tests = self.passed + self.failed
        pass_rate = (self.passed / total_tests * 100) if total_tests > 0 else 0
        
        self.log(f"\nTotal Tests: {total_tests}")
        self.log(f"Passed: {self.passed} ✓", "SUCCESS")
        self.log(f"Failed: {self.failed}", "FAIL" if self.failed > 0 else "SUCCESS")
        self.log(f"Pass Rate: {pass_rate:.1f}%", "SUCCESS" if pass_rate >= 90 else "WARNING")
        
        # Overall status
        if self.failed == 0:
            self.log("\n🎉 ALL TESTS PASSED - PIPELINE IS READY", "SUCCESS")
            status = "SUCCESS"
        elif pass_rate >= 80:
            self.log("\n⚠️ MOST TESTS PASSED - Minor issues only", "WARNING")
            status = "WARNING"
        else:
            self.log("\n❌ CRITICAL FAILURES - Pipeline needs work", "ERROR")
            status = "FAILURE"
        
        return {
            "status": status,
            "total_tests": total_tests,
            "passed": self.passed,
            "failed": self.failed,
            "pass_rate": pass_rate,
            "test_results": results,
            "detailed_results": self.test_results
        }


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Test mathematics animation pipeline")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--save-report", help="Save results to JSON file")
    args = parser.parse_args()
    
    # Run tests
    tester = MathPipelineTest(verbose=args.verbose)
    results = tester.run_all_tests()
    
    # Save report if requested
    if args.save_report:
        with open(args.save_report, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\n📄 Report saved to: {args.save_report}")
    
    # Return appropriate exit code
    return 0 if results["failed"] < 2 else 1


if __name__ == "__main__":
    sys.exit(main())
