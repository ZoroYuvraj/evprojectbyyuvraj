# 5–7 Minute Project Walkthrough Script

Use this as a speaking outline while recording the project screen. Replace bracketed notes after the Tableau workbook is complete.

## 0:00–0:40 — Introduce the project

“Hello, I’m Yuvraj Devda. My project is **Electric Vehicle Market Performance & Insights**. I use Tableau to explore how the supplied EV records compare across vehicle category, manufacturer, model year, battery technology, and market region. The main question is: what patterns are visible in the recorded sales measure and vehicle specifications?”

## 0:40–1:30 — Explain the data

“The training file contains 200,000 rows and 37 columns, and the test file contains 100,000 rows with the same fields. The columns include model year, category, manufacturer, battery capacity/type, range, price, rating, and annual sales units. The source and collection method were not included with the files, so I treat the data as an educational dataset and do not present the results as verified global market facts.”

## 1:30–2:15 — Describe preparation

“I checked the schema, missing values, and duplicate IDs using the included profile script. The training file has one repeated vehicle ID and missing values in several measures, including resale value, customer rating, battery cycle life, and annual sales units. I left unknown values blank instead of replacing them with zero, and I used distinct vehicle IDs for unique-record counts.”

## 2:15–4:30 — Show the dashboard

“The dashboard has four views. The category chart compares the recorded annual sales measure across vehicle classes. The manufacturer chart is limited to the top 10 labels by the same measure. The model-year line chart shows how the measure varies across years, and the battery chart compares battery types. Selecting a category in the dashboard can filter the other views. These are patterns in the supplied file; the dataset's source and definitions are unconfirmed.”

Demonstrate the Category filter on the category worksheet and the dashboard category selection action. Clear the selection before moving on. Do not mention KPI cards, a map, or a scatter plot as completed—the current workbook does not contain them.

## 4:30–5:30 — Present findings

“In the training file, the highest summed category is [category/value], and the highest manufacturer label is [manufacturer/value]. Average range is [value] km and average battery capacity is [value] kWh. These are summaries of this file; I do not treat the sales units or rating scale as independently validated.”

## 5:30–6:15 — Show the story and close

“The Tableau Story has six scenes: the dashboard overview, annual sales trend, category comparison, top manufacturers, battery mix, and average ratings by category. The main limitation is missing data provenance and field definitions. With a verified source and definitions, this analysis could be refreshed and compared with authoritative market data. Thank you.”

## Before recording

- Replace all bracketed prompts and rehearse once.
- Keep the dashboard visible at readable zoom and clear filters before recording.
- Show the project repository and mention where the guide and profile are stored.
- Mention that KPI cards and a geographic map are not included yet. The customer-rating worksheet and Story scene are included.
- Do not expose login credentials, private account details, or unpublished tokens in the recording.
