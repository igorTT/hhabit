"""
Documentation fitness evaluation tool for test files.
Evaluates the quality of test documentation based on defined metrics.
"""

import ast
from pathlib import Path
from typing import Dict, List, Tuple
import re


class DocFitnessEvaluator:
    def __init__(self, test_dir: str = "tests"):
        self.test_dir = Path(test_dir)
        self.metrics = {
            "completeness": 0.0,
            "clarity": 0.0,
            "structure": 0.0,
            "maintainability": 0.0
        }

    def evaluate_file(self, file_path: Path) -> Dict[str, float]:
        """Evaluate documentation quality for a single test file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse the Python file
        tree = ast.parse(content)

        # Get module docstring
        module_doc = ast.get_docstring(tree)

        # Get all function definitions
        functions = [node for node in ast.walk(
            tree) if isinstance(node, ast.FunctionDef)]

        # Get all fixture definitions
        fixtures = [node for node in functions if any(
            decorator.id == 'fixture'
            for decorator in node.decorator_list
            if isinstance(decorator, ast.Name)
        )]

        # Calculate metrics
        completeness = self._calculate_completeness(
            module_doc, functions, fixtures)
        clarity = self._calculate_clarity(module_doc, functions, fixtures)
        structure = self._calculate_structure(module_doc, functions, fixtures)
        maintainability = self._calculate_maintainability(content)

        return {
            "completeness": completeness,
            "clarity": clarity,
            "structure": structure,
            "maintainability": maintainability
        }

    def _calculate_completeness(self, module_doc: str, functions: List[ast.FunctionDef],
                                fixtures: List[ast.FunctionDef]) -> float:
        """Calculate completeness score based on presence of required documentation."""
        score = 0.0
        total_checks = 0

        # Check module docstring
        if module_doc:
            score += 1
        total_checks += 1

        # Check function docstrings
        for func in functions:
            if ast.get_docstring(func):
                score += 1
            total_checks += 1

        # Check fixture docstrings
        for fixture in fixtures:
            if ast.get_docstring(fixture):
                score += 1
            total_checks += 1

        return (score / total_checks) * 100 if total_checks > 0 else 0.0

    def _calculate_clarity(self, module_doc: str, functions: List[ast.FunctionDef],
                           fixtures: List[ast.FunctionDef]) -> float:
        """Calculate clarity score based on documentation quality."""
        score = 0.0
        total_checks = 0

        # Check module docstring clarity
        if module_doc:
            if len(module_doc.split('\n')) > 1:  # Multiple lines
                score += 1
            if any(section in module_doc.lower() for section in ['purpose', 'test', 'component']):
                score += 1
            total_checks += 2

        # Check function docstrings
        for func in functions:
            doc = ast.get_docstring(func)
            if doc:
                if len(doc.split('\n')) > 3:  # Multiple sections
                    score += 1
                if any(section in doc.lower() for section in ['expected', 'precondition', 'postcondition']):
                    score += 1
                total_checks += 2

        # Check fixture docstrings
        for fixture in fixtures:
            doc = ast.get_docstring(fixture)
            if doc:
                if 'returns' in doc.lower():
                    score += 1
                if 'note' in doc.lower():
                    score += 1
                total_checks += 2

        return (score / total_checks) * 100 if total_checks > 0 else 0.0

    def _calculate_structure(self, module_doc: str, functions: List[ast.FunctionDef],
                             fixtures: List[ast.FunctionDef]) -> float:
        """Calculate structure score based on documentation organization."""
        score = 0.0
        total_checks = 0

        # Check module docstring structure
        if module_doc:
            if re.search(r'^[A-Z]', module_doc):  # Starts with capital letter
                score += 1
            if re.search(r'\.$', module_doc):  # Ends with period
                score += 1
            total_checks += 2

        # Check function docstrings
        for func in functions:
            doc = ast.get_docstring(func)
            if doc:
                if re.search(r'^[A-Z]', doc):  # Starts with capital letter
                    score += 1
                if re.search(r'\.$', doc):  # Ends with period
                    score += 1
                total_checks += 2

        # Check fixture docstrings
        for fixture in fixtures:
            doc = ast.get_docstring(fixture)
            if doc:
                if re.search(r'^[A-Z]', doc):  # Starts with capital letter
                    score += 1
                if re.search(r'\.$', doc):  # Ends with period
                    score += 1
                total_checks += 2

        return (score / total_checks) * 100 if total_checks > 0 else 0.0

    def _calculate_maintainability(self, content: str) -> float:
        """Calculate maintainability score based on code and documentation patterns."""
        score = 0.0
        total_checks = 0

        # Check for TODO comments
        if not re.search(r'TODO', content):
            score += 1
        total_checks += 1

        # Check for consistent indentation
        lines = content.split('\n')
        indentation_levels = set()
        for line in lines:
            if line.strip():
                indentation_levels.add(len(line) - len(line.lstrip()))
        if len(indentation_levels) <= 2:  # Consistent indentation
            score += 1
        total_checks += 1

        # Check for long lines
        long_lines = sum(1 for line in lines if len(line) > 100)
        if long_lines == 0:
            score += 1
        total_checks += 1

        return (score / total_checks) * 100 if total_checks > 0 else 0.0

    def evaluate_all(self) -> Tuple[Dict[str, float], List[Tuple[Path, Dict[str, float]]]]:
        """Evaluate all test files in the test directory."""
        file_scores = []
        total_metrics = {
            "completeness": 0.0,
            "clarity": 0.0,
            "structure": 0.0,
            "maintainability": 0.0
        }
        total_files = 0

        for file_path in self.test_dir.rglob("test_*.py"):
            metrics = self.evaluate_file(file_path)
            file_scores.append((file_path, metrics))

            for metric in total_metrics:
                total_metrics[metric] += metrics[metric]
            total_files += 1

        # Calculate averages
        if total_files > 0:
            for metric in total_metrics:
                total_metrics[metric] /= total_files

        return total_metrics, file_scores

    def print_report(self, total_metrics: Dict[str, float],
                     file_scores: List[Tuple[Path, Dict[str, float]]]) -> None:
        """Print a formatted report of the documentation evaluation."""
        print("\nDocumentation Fitness Report")
        print("=" * 50)

        print("\nOverall Metrics:")
        for metric, score in total_metrics.items():
            print(f"{metric.capitalize()}: {score:.2f}%")

        fitness_score = sum(total_metrics.values()) / len(total_metrics)
        print(f"\nOverall Fitness Score: {fitness_score:.2f}%")

        print("\nFile-Specific Scores:")
        for file_path, metrics in file_scores:
            print(f"\n{file_path}:")
            for metric, score in metrics.items():
                print(f"  {metric.capitalize()}: {score:.2f}%")


def main():
    """Main entry point for the documentation fitness evaluation."""
    evaluator = DocFitnessEvaluator()
    total_metrics, file_scores = evaluator.evaluate_all()
    evaluator.print_report(total_metrics, file_scores)


if __name__ == "__main__":
    main()
