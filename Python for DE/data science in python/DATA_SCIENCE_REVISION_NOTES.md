# Data Science in Python: Professional Revision Notes

A revision guide for this folder, moving from basic Python execution to small machine-learning applications and Streamlit interfaces.

## 1. Learning Roadmap

The folder follows this progression:

1. Run simple Python code in a notebook.
2. Generate a reproducible numerical dataset with NumPy and Pandas.
3. Train and visualize a linear regression model.
4. Put the regression model inside a Streamlit app.
5. Generate a small labeled text dataset.
6. Train a text-classification pipeline with TF-IDF and logistic regression.
7. Put the classifier inside a Streamlit app.
8. Build a content-based book recommendation system with TF-IDF and cosine similarity.

The common data-science workflow is:

```text
Question -> Data -> Cleaning -> Exploration -> Features -> Model
         -> Evaluation -> Interface or deployment -> Monitoring
```

The examples demonstrate most of this workflow, but they are educational prototypes rather than production systems.

---

## 2. File-by-File Guide

### `1_basic.ipynb`: Notebook fundamentals

This notebook is an introduction to executing Python in cells.

Concepts covered:

- `print()` displays values.
- Arithmetic expressions are evaluated immediately.
- `range(1, 11)` produces integers from 1 through 10 because the stop value is exclusive.
- A `for` loop repeats a block of code.
- Notebook cells can contain Python code or Markdown explanations.
- Execution order matters: variables created in an earlier cell may be used later.
- The notebook metadata selects Python 3.12.10.

Important practice:

- Run cells from top to bottom when possible.
- Restart the kernel and run all cells to detect hidden state dependencies.
- Keep explanations close to the code they explain.
- The notebook has saved outputs, but its current metadata says the cells are not executed in the current session. Saved output is not proof that the notebook currently runs successfully.

Example interpretation:

```python
for number in range(1, 11):
    print(number * 2)
```

This prints the first ten positive even numbers.

---

### `2_generate_dataset.py`: Synthetic salary data

Purpose: create a small, predictable dataset for regression practice.

```python
np.random.seed(42)
years = np.random.uniform(0.5, 10, 100).round(2)
salary = (30000 + years * 6000 + np.random.normal(0, 4000, 100)).round(2)
```

Meaning of the formula:

- `30000` is the approximate starting salary, or intercept.
- `6000` is the approximate salary increase per year of experience, or slope.
- `np.random.uniform(0.5, 10, 100)` creates 100 experience values between 0.5 and 10.
- `np.random.normal(0, 4000, 100)` adds normally distributed noise with mean 0 and standard deviation 4000.
- `np.random.seed(42)` makes the random output reproducible.
- `.round(2)` keeps values readable but does not improve model quality.
- `pd.DataFrame(...)` creates a table with named columns.
- `to_csv(..., index=False)` saves the table without Pandas' index column.

Expected relationship:

$$salary \approx 30000 + 6000 \times years\_of\_experience + noise$$

Critical correction:

```python
# Correct approach
 df = pd.DataFrame({"years_of_experience": years, "salary": salary})
 df.to_csv("data.csv", index=False)
 df.to_csv("exp_salaries.csv", index=False)
```

`DataFrame.to_csv()` writes the file and returns `None`; it does not return another DataFrame. The current script assigns that `None` value back to `df` and then calls `df.to_csv(...)`, which causes an `AttributeError`. The existing `data.csv` is usable, but regenerating it with the current script will fail.

Revision questions:

- Why is a seed useful in a tutorial or experiment?
- What happens if the noise standard deviation changes from 4000 to 20000?
- Why should a real salary dataset include location, industry, education, role, and seniority rather than experience alone?

---

### `3_project_liner_regression.py`: Linear regression

Purpose: learn a line that predicts salary from years of experience.

Important objects:

- `data`: the DataFrame loaded from `data.csv`.
- `x`: the feature matrix, selected as a two-dimensional DataFrame using `[[...]]`.
- `y`: the target vector, selected as a one-dimensional Series.
- `LinearRegression()`: scikit-learn's ordinary least-squares linear regression estimator.
- `model.fit(x, y)`: estimates the best intercept and coefficient.
- `model.predict(x)`: calculates predicted salaries.
- `model.coef_[0]`: estimated salary change for one additional year of experience.
- `model.intercept_`: estimated salary when experience is zero.

Model form:

$$\hat{y} = b_0 + b_1x$$

For this project:

- $\hat{y}$ is predicted salary.
- $b_0$ is the intercept.
- $b_1$ is the experience coefficient.
- $x$ is years of experience.

Visualization:

- `plt.scatter(...)` displays actual observations.
- `plt.plot(...)` displays model predictions.
- Labels, title, legend, grid, and `tight_layout()` improve readability.
- `plt.show()` opens the chart.

What to improve:

- Split into training and test data before fitting.
- Report MAE, RMSE, and $R^2$ rather than only plotting the fitted values.
- Plot a sorted feature column or use a line generated from evenly spaced values. The current `x` values are not sorted, so connecting predictions in row order can make the regression line look zigzagged.
- Avoid evaluating the model on the same rows used to fit it.
- Validate assumptions such as linearity, independent errors, and reasonably stable variance.

Useful metrics:

$$MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|$$

$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}$$

$$R^2 = 1 - \frac{\sum(y_i - \hat{y}_i)^2}{\sum(y_i - \bar{y})^2}$$

Interpretation: a coefficient is an association learned from the supplied data, not proof that experience alone causes salary increases.

---

### `4_stream_lit_salaryprediction.py`: Regression with Streamlit

Purpose: expose the salary model through a browser-based user interface.

Streamlit concepts:

- `st.title`, `st.write`, and `st.subheader` render text.
- `st.number_input` collects numeric input with minimum, maximum, and step constraints.
- `st.success` displays a positive result message.
- `st.pyplot(fig)` displays a Matplotlib figure.
- The script reruns from top to bottom whenever a widget changes.

Prediction flow:

1. Load `data.csv`.
2. Fit the regression model.
3. Read the user's experience value.
4. Call `model.predict(...)`.
5. Format the predicted salary with commas and two decimals.

What to improve:

- Use a DataFrame with the same feature name when predicting to avoid scikit-learn feature-name warnings:

```python
input_data = pd.DataFrame({"years_of_experience": [years_of_experience]})
 predicted_salary = model.predict(input_data)[0]
```

- The current `if years_of_experience > 0` means an allowed value of exactly 0 produces no result. Either set the minimum to a positive value or allow zero and display its prediction.
- Cache the loaded data and trained model with `@st.cache_data` and `@st.cache_resource` when appropriate.
- Train on a saved model in a larger application instead of fitting on every rerun.
- Add a test-set metric so users can see model quality, not just one prediction.
- Treat the result as an estimate, not a guaranteed salary.

Run with:

```text
streamlit run 4_stream_lit_salaryprediction.py
```

Run the command from this folder, or use an explicit path to `data.csv` if the working directory differs.

---

### `5_small_nlp_project.py`: Synthetic comment data

Purpose: create a labeled dataset for toxic/supportive comment classification.

Key ideas:

- A list of text examples is created for each class.
- `random.choice(...)` samples one item from each list.
- Each record is a dictionary with `comment` and `label` fields.
- A list of dictionaries becomes a DataFrame.
- The result is saved as `youtube_comments.csv`.

The loop creates 50 toxic and 50 supportive rows, so the intended class balance is 50/50. However, comments repeat because sampling is with replacement. This is useful for demonstrating file and model pipelines, but it is not a realistic training dataset.

What to improve:

- Set `random.seed(42)` for reproducibility.
- Use a larger, independently labeled dataset.
- Include neutral, ambiguous, sarcastic, multilingual, and misspelled examples.
- Define labeling rules and measure inter-rater agreement.
- Consider privacy, moderation policy, and false-positive harm before deploying a toxicity classifier.

---

### `6_logstic.py`: TF-IDF plus logistic regression

Purpose: classify a comment as `toxic` or `support`.

Pipeline:

```text
raw comment -> TfidfVectorizer -> numeric sparse features -> LogisticRegression -> label
```

Key concepts:

- `train_test_split` separates data for training and evaluation.
- `test_size=0.2` reserves 20% for the test set.
- `random_state=42` makes the split reproducible.
- `TfidfVectorizer` converts text into weighted word features.
- `stop_words="english"` can remove common English words, though the default in this file is not configured.
- `Pipeline` keeps transformation and prediction together and reduces train/test preprocessing mistakes.
- `LogisticRegression` learns class probabilities or a decision boundary for classification.
- `model.score(...)` returns accuracy for this classifier.

TF-IDF intuition:

- TF measures how often a term appears in a document.
- IDF reduces the weight of terms appearing in many documents.
- A word that is frequent in one comment but uncommon across all comments receives a stronger distinguishing weight.

Cosine similarity is also useful for comparing vectors, but this classifier is supervised: it learns from labels. The recommendation app is unsupervised/content-based: it compares item descriptions without target labels.

What to improve:

- Use `stratify=df["label"]` in `train_test_split` to preserve class balance.
- Report a confusion matrix, precision, recall, and F1 score.
- Accuracy can be misleading when classes are imbalanced.
- Because the dataset repeats a small number of phrases, a random split may place identical text in both training and test sets. The reported accuracy can therefore be unrealistically high.
- Evaluate on unique comments or collect a genuinely independent test set.
- Set `max_iter` explicitly if a larger real dataset causes convergence warnings.

Metrics:

- Precision: among predicted toxic comments, how many are toxic?
- Recall: among truly toxic comments, how many were detected?
- F1: harmonic mean of precision and recall.
- Confusion matrix: counts true positives, true negatives, false positives, and false negatives.

Run with:

```text
python 6_logstic.py
```

The filename contains a spelling mistake (`logstic`); it does not affect Python execution, but a clearer name would be `6_logistic.py`.

---

### `7_streamlitfy.py`: Streamlit comment analyzer

Purpose: provide a text box that classifies a user-entered comment.

Key concepts:

- `@st.cache_resource` caches the trained model between reruns.
- The model is built from the same TF-IDF and logistic-regression pipeline used in file 6.
- `st.text_area` accepts multiline text.
- `model.predict([user_input])` predicts one comment.
- `st.error` and `st.success` show class-specific feedback.

What to improve:

- Cache the dataset separately with `st.cache_data` if the data-loading step becomes expensive.
- Display confidence with `predict_proba`, but explain that model confidence is not certainty.
- Handle blank or whitespace-only input with `user_input.strip()`.
- Preserve more neutral language: a model prediction should not automatically be treated as a final moderation decision.
- Add a model evaluation section and examples of false positives/false negatives.
- Keep training and inference code in separate modules as the project grows.

Run with:

```text
streamlit run 7_streamlitfy.py
```

---

### `8_generatedatset_for_recomdation_engine.py`: Book recommendation engine

Purpose: recommend books whose descriptions are textually similar to a selected book.

Data:

- `books.csv` contains title, genre, author, and description.
- The dataset has 20 books and a small number of repeated genres.
- Descriptions are the item features used by the recommender.

Processing flow:

1. `@st.cache_data` caches the CSV loading step.
2. `TfidfVectorizer(stop_words="english")` converts descriptions into sparse vectors.
3. `cosine_similarity(tfidf_matrix, tfidf_matrix)` compares every book with every other book.
4. A title-to-index Series maps a selected title to its row.
5. `get_recommendation` obtains the selected row's similarity scores.
6. Scores are sorted from highest to lowest.
7. The selected book is removed because its similarity with itself is 1.
8. The top requested rows are returned with a similarity percentage.
9. Streamlit renders metadata, the selected book, and recommendation cards.

Cosine similarity:

$$cos(\theta) = \frac{A \cdot B}{||A|| ||B||}$$

For normalized TF-IDF vectors, a higher score means the descriptions share more weighted terms. It does not mean that readers will definitely like the recommended book.

Streamlit concepts demonstrated:

- `st.set_page_config` controls page title, icon, and layout.
- `@st.cache_data` is suitable for loaded data.
- `@st.cache_resource` is suitable for reusable model artifacts.
- `st.sidebar`, `selectbox`, `slider`, and `button` create controls.
- `st.columns`, `st.metric`, `st.container(border=True)`, and `st.divider` organize the interface.
- `iterrows()` renders each recommendation row.

What to improve:

- The `vectorizer` is returned but not used after model creation; return only what is needed or use it for new-item/query recommendations.
- Duplicate titles would make `indices[title]` ambiguous. Enforce unique titles or map titles to lists of indexes.
- Validate missing or empty descriptions before fitting TF-IDF.
- With only 20 books, recommendations are a demonstration, not a reliable production engine.
- Similarity percentages are presentation values, not probabilities or quality scores.
- The current system cannot recommend a new book unless its description is added and the model is rebuilt.
- Add recommendation tests: known title, missing title, requested count larger than the dataset, and empty descriptions.
- For a larger catalog, do not materialize the full $n \times n$ similarity matrix without considering memory; retrieve nearest neighbors or use a vector database.

Run with:

```text
streamlit run 8_generatedatset_for_recomdation_engine.py
```

The filename has spelling issues (`generatedatset`, `recomdation`), so a future cleanup could rename it to `8_book_recommendation_engine.py`.

---

## 3. Dataset Notes

### `data.csv`

- Columns: `years_of_experience`, `salary`.
- 100 rows of synthetic numerical data.
- Intended for one-feature regression.
- Salary is approximately positively related to experience with random noise.
- Do not treat this as a real labor-market dataset.

Recommended checks:

```python
print(data.shape)
print(data.dtypes)
print(data.isna().sum())
print(data.describe())
```

### `youtube_comments.csv`

- Columns: `comment`, `label`.
- 100 rows intended to be balanced between `toxic` and `support`.
- Repeated phrases are common.
- The labels are synthetic and simplistic.
- It is appropriate for learning a pipeline, not for making moderation decisions.

Recommended checks:

```python
print(df["label"].value_counts())
print(df["comment"].nunique())
print(df.isna().sum())
```

### `books.csv`

- Columns: `title`, `genre`, `author`, `description`.
- 20 book records.
- Used for content-based recommendations.
- No user ratings, clicks, purchases, or feedback are present, so this is not collaborative filtering.

---

## 4. Core Concepts to Memorize

### Pandas

- `pd.read_csv(path)`: load a CSV as a DataFrame.
- `DataFrame(...)`: create tabular data.
- `df[["column"]]`: select a DataFrame with one column.
- `df["column"]`: select a Series.
- `df.iloc[indexes]`: select rows by integer position.
- `df.nunique()`: count distinct values.
- `df.to_csv(path, index=False)`: save a DataFrame.

### NumPy

- `np.random.seed`: control reproducibility.
- `np.random.uniform`: sample from a uniform distribution.
- `np.random.normal`: sample from a normal distribution.
- Vectorized arithmetic applies an operation to an entire array without a manual loop.

### Scikit-learn

- Estimator lifecycle: create -> `fit` -> `predict`/`transform` -> evaluate.
- A feature matrix is usually shaped `(number_of_rows, number_of_features)`.
- A target is usually shaped `(number_of_rows,)`.
- A pipeline prevents inconsistent preprocessing between training and inference.
- Always separate training data from evaluation data.

### Text representation

- Machines need numbers, not raw text.
- TF-IDF creates a weighted vocabulary representation.
- Sparse matrices save memory because most word-document entries are zero.
- Vocabulary quality, dataset size, and labels strongly affect model quality.

### Streamlit

- A Streamlit script reruns when widget state changes.
- Use `cache_data` for data and `cache_resource` for models or expensive reusable resources.
- Keep the UI layer thin and move reusable data/model logic into functions or modules.
- Validate user inputs before prediction.

---

## 5. Recommended Corrections Before Reusing the Folder

1. Fix `2_generate_dataset.py` so the DataFrame is not overwritten by `to_csv()`.
2. Add train/test evaluation to the linear regression example.
3. Sort plotting values or draw the regression line from a regular grid.
4. Use named DataFrame input for salary prediction.
5. Seed the random comment generator.
6. Use stratification and richer metrics for comment classification.
7. Test the classifier on unique or independently collected comments.
8. Validate empty descriptions and duplicate titles in the recommender.
9. Rename files with spelling mistakes when the learning phase is complete.
10. Add a `requirements.txt` containing the packages used by the folder:

```text
pandas
numpy
matplotlib
scikit-learn
streamlit
```

Do not install packages blindly in production; pin versions after confirming the Python environment.

---

## 6. Practical Revision Exercises

### Beginner

1. Change the notebook loop to print squares from 1 through 10.
2. Load `data.csv` and calculate the average salary.
3. Count toxic and supportive comments.
4. Display the number of books per genre.

### Intermediate

1. Repair and run the dataset generator.
2. Add a train/test split and MAE to the salary model.
3. Add `stratify` and a confusion matrix to the text classifier.
4. Add a text input to the recommendation app and recommend based on a new description.
5. Add a checkbox to show or hide book descriptions.

### Advanced

1. Compare linear regression with a tree-based regressor.
2. Use cross-validation for both regression and classification.
3. Tune TF-IDF parameters such as `ngram_range`, `min_df`, and `max_features`.
4. Compare accuracy, precision, recall, and F1 under class imbalance.
5. Build a hybrid recommender using genre, author, and description.
6. Persist the trained model with `joblib` and load it in Streamlit.
7. Add tests for every public function and edge case.

---

## 7. Final Revision Checklist

Before considering this folder mastered, be able to explain and demonstrate:

- [ ] Why `range` excludes its stop value.
- [ ] Why a random seed makes an experiment reproducible.
- [ ] The difference between a DataFrame and a Series.
- [ ] The difference between a feature matrix and a target vector.
- [ ] What a regression coefficient and intercept mean.
- [ ] Why evaluating on training data is insufficient.
- [ ] The meaning of MAE, RMSE, and $R^2$.
- [ ] How TF-IDF changes text into numeric features.
- [ ] Why a `Pipeline` is useful.
- [ ] The difference between accuracy, precision, recall, and F1.
- [ ] Why repeated phrases can cause data leakage.
- [ ] The difference between supervised classification and content-based recommendation.
- [ ] How cosine similarity ranks similar documents.
- [ ] The difference between `st.cache_data` and `st.cache_resource`.
- [ ] Why a Streamlit app reruns when widgets change.
- [ ] How to test missing input, duplicate records, and empty data.

## One-Sentence Summary

This folder teaches the end-to-end shape of a small data-science application: create or load data, represent it numerically, train a model or similarity system, measure its behavior honestly, and expose the result through a usable interface.
