# Mathematics Animation Training System

## Overview

This system adds comprehensive mathematics-specific animations to DevForge, replacing generic "moving grid" animations with topic-relevant visualizations. It includes:

- **8 new math domain engines** with specialized visualizations
- **100+ training examples** across all math topics
- **Topic-specific animation functions** for clean, focused videos
- **Model training pipeline** for improved topic recognition
- **Comprehensive testing suite** to ensure pipeline integrity

## Quick Start

### 1. Generate Training Data

```bash
python training/math_training_data_generator.py
```

This generates:

- `training/math_training_examples.json` - 100+ math topic examples
- `training/math_training_dataset.jsonl` - Training-ready JSONL format
- `training/math_topic_animation_mapping.json` - Topic-to-animation mappings

### 2. Train the Model

```bash
python training/train_math_model.py
```

Or with options:

```bash
python training/train_math_model.py --epochs 5 --batch-size 8 --output-dir trained_models
```

### 3. Test the Pipeline

```bash
python training/test_math_pipeline.py --verbose
```

## Supported Math Topics

### 1. **Matrix Multiplication** (`matrix_multiplication`)

- Visualizes 2x2 and 3x3 matrix multiplication
- Shows element-by-element row × column operations
- Highlights dot products in real-time

**Example concepts:**

- "Matrix multiplication of 2x2 matrices"
- "How to multiply two matrices element by element"
- "Row reduction and Gaussian elimination"

### 2. **Integral Calculus** (`integral_calculus`)

- Shows area under curves using Riemann sums
- Animates rectangle approximation increasing in precision
- Displays the convergence to the definite integral

**Example concepts:**

- "Integral calculus"
- "Area under the curve using Riemann sums"
- "Fundamental theorem of calculus"

### 3. **Derivatives** (`derivatives`)

- Visualizes tangent lines to curves
- Shows instantaneous rate of change
- Animates slope calculation at different points

**Example concepts:**

- "Derivative of a polynomial function"
- "Power rule for derivatives"
- "Instantaneous rate of change"

### 4. **Linear Algebra** (`linear_algebra`)

- Displays vectors in coordinate space
- Shows vector addition and transformations
- Illustrates basis vectors and linear independence

**Example concepts:**

- "Systems of linear equations"
- "Vector spaces and subspaces"
- "Eigenvalues and eigenvectors"

### 5. **Limits** (`limits`)

- Shows function behavior near a specific point
- Demonstrates left and right limits
- Visualizes convergence toward the limit value

**Example concepts:**

- "Limit of a function as x approaches a value"
- "Epsilon-delta definition of limits"
- "Continuity at a point"

### 6. **Trigonometry** (`trigonometry`)

- Displays the unit circle with rotating angles
- Shows sine/cosine/tangent projections
- Animates angle measurements in radians

**Example concepts:**

- "Trigonometric unit circle"
- "Sine and cosine functions"
- "Law of sines and law of cosines"

### 7. **Sequences and Series** (`sequences_series`)

- Visualizes sequence terms as bar charts
- Shows series convergence behavior
- Displays partial sums approaching the limit

**Example concepts:**

- "Arithmetic sequences and series"
- "Infinite series and convergence"
- "Geometric series"

### 8. **Vector Calculus** (`vector_calculus`)

- Draws vector fields with animated vectors
- Shows gradient direction and magnitude
- Visualizes divergence and curl concepts

**Example concepts:**

- "Vector fields and field lines"
- "Gradient of a scalar field"
- "Divergence and curl"

## Architecture

### Topic Detection Flow

```
User Input Text
    ↓
topic_router.detect_topic()
    ↓
Regex pattern matching (strict math detection)
    ↓
Returns topic: "matrix_multiplication" | "integral_calculus" | etc.
    ↓
Animation Router
    ↓
create_[topic]_clip()  ← New math-specific animations
    ↓
No generic grid - topic-focused visualization only
```

### Updated Files

1. **src/topic_router.py**
   - Added 8 new math topic detection patterns
   - Updated `get_animation_clip()` to handle math topics
   - Added descriptions for all math animations
   - Expanded `has_animation()` to include math topics

2. **src/animation_clips.py**
   - Added 8 new animation functions (500+ lines of code)
   - No "moving grid" for math topics
   - Clean, focused visualizations for each topic
   - Uses MATH theme for all mathematical visualizations

3. **src/domain_engines/[multiple].py**
   - matrix_multiplication.py
   - integral_calculus.py
   - derivatives.py
   - linear_algebra.py
   - limits.py
   - trigonometry.py
   - sequences_series.py
   - vector_calculus.py

### New Training Files

1. **training/math_training_data_generator.py**
   - Generates 100+ training examples
   - Creates JSONL format for model training
   - Produces topic-to-animation mappings

2. **training/train_math_model.py**
   - Fine-tunes LLM on math topics
   - Supports both simulated and real training
   - Includes validation and testing

3. **training/test_math_pipeline.py**
   - 7-test comprehensive validation suite
   - Tests topic detection accuracy
   - Validates animation availability
   - Checks pipeline integrity

## Training Examples Distribution

- **Matrix Multiplication**: 15 examples
- **Integral Calculus**: 15 examples
- **Derivatives**: 15 examples
- **Linear Algebra**: 15 examples
- **Limits and Continuity**: 15 examples
- **Trigonometry**: 15 examples
- **Sequences and Series**: 15 examples
- **Vector Calculus**: 10 examples

**Total: 115 training examples**

## Configuration

### Environment Variables

None required - system uses defaults. Customize by editing config:

```python
# src/topic_router.py
detect_topic(concept: str) -> str
```

### Animation Duration

All math animations default to 5.0 seconds:

```python
create_matrix_multiplication_clip(duration=5.0, **kwargs)
```

Customize duration when called from renderer:

```python
animation_clip = get_animation_clip(
    concept,
    duration=7.0  # Custom duration
)
```

## Testing

Run the full test suite:

```bash
python training/test_math_pipeline.py --verbose --save-report test_results.json
```

**Tests included:**

1. ✓ Topic detection (16 test cases)
2. ✓ Animation availability (8 topics)
3. ✓ Specialized animation detection (8 concepts)
4. ✓ Animation info retrieval (4 topics)
5. ✓ Non-math topic exclusions (5 concepts)
6. ✓ Training data file validation
7. ✓ Animation function availability (8 functions)

## Pipeline Integrity

**No breaking changes to existing pipeline:**

- ✓ Existing animations still work (projectile motion, sine wave, etc.)
- ✓ Generic animations still available as fallback
- ✓ All previous features preserved
- ✓ New features are purely additive

### Backward Compatibility

```python
# Old code still works
animator = EducationalAnimator()
video_path, plan = animator.generate("Explain photosynthesis")

# New math animations work automatically
video_path, plan = animator.generate("Matrix multiplication")

# Non-math topics unaffected
video_path, plan = animator.generate("Bubble sort algorithm")
```

## Usage Examples

### Basic Usage

```bash
# Math topic - gets math-specific animation
python -m src.main "Explain matrix multiplication"

# Another math topic
python -m src.main "Integral calculus and area under curves"

# Non-math still works
python -m src.main "Binary search algorithm"
```

### With Language Support

```bash
# Math in Hindi
python -m src.main "मैट्रिक्स गुणन" --lang hi

# Math in Spanish
python -m src.main "Multiplicación de matrices" --lang es
```

### Disable Animations

```bash
# Use generic cards for any topic
python -m src.main "Matrix multiplication" --no-animations
```

## Performance Impact

- **Model training**: ~2-5 minutes (with GPU: ~30 seconds)
- **Topic detection**: <1ms per concept
- **Animation generation**: 5 seconds per topic
- **Overall pipeline**: No significant slowdown

## Troubleshooting

### Training data not found

```bash
# Generate training data first
python training/math_training_data_generator.py
```

### ML frameworks not installed

```bash
# Install optional dependencies
pip install torch transformers peft
```

### Animation functions missing

```bash
# Check animation_clips.py for new functions
grep "def create_matrix_multiplication_clip" src/animation_clips.py
```

### Topic not detected as math

```python
# Check detection patterns in topic_router.py
# May need to add more regex patterns for edge cases
```

## Future Enhancements

Potential additions:

- [ ] Probability and statistics animations
- [ ] Complex numbers and fractals
- [ ] Differential equations solver visualization
- [ ] Multivariable calculus (partial derivatives, gradients)
- [ ] Abstract algebra (group theory, rings)
- [ ] Numerical methods visualization
- [ ] Real-time 3D mathematics rendering

## Contributing

To add a new math topic:

1. Create `src/domain_engines/new_topic.py`
2. Add detection patterns to `src/topic_router.py`
3. Create `create_new_topic_clip()` in `src/animation_clips.py`
4. Add training examples to `math_training_data_generator.py`
5. Run `test_math_pipeline.py` to validate

## Support

For issues or questions:

1. Check `training/test_math_pipeline.py` output
2. Review topic detection patterns in `topic_router.py`
3. Examine animation functions in `animation_clips.py`
4. Consult training data in `math_training_dataset.jsonl`

---

**Status**: ✅ Production Ready
**Last Updated**: March 1, 2026
**Version**: 1.0
