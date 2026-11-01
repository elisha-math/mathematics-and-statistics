# Data Cleaning Report

## 1. Overview

This report documents the data quality assessment and cleaning process for the Online Retail dataset used in the Retail Sales and Customer Behaviour Analysis project.

The original dataset contains 541,909 transaction records from a UK-based online retailer, covering transactions between December 2010 and December 2011.

The purpose of cleaning was to prepare the data for reliable sales analysis while preserving the original records and documenting decisions made during the process.

## 2. Original Dataset

The original dataset contained:

- Records: 541,909
- Columns: 8
- Missing product descriptions: 1,454
- Missing customer IDs: 135,080
- Duplicate records: 5,268

The dataset includes invoice information, product codes, descriptions, quantities, transaction dates, unit prices, customer IDs and countries.

## 3. Duplicate Records

A total of 5,268 exact duplicate records were identified and removed.

After removal, the dataset contained 536,641 records.

The original dataset was preserved separately to maintain traceability and allow comparison with the cleaned data.

## 4. Missing Values

Two columns contained missing values:

- Description: 1,454 missing values.
- CustomerID: 135,037 missing values after duplicate removal.

Records with missing customer IDs were retained for overall sales analysis because they may still contain valid transaction information.

However, these records cannot reliably be assigned to individual customers. They are therefore excluded from customer-level analysis where customer identification is required.

Records with missing descriptions were also retained in the general cleaned dataset. No product descriptions were invented or filled in without evidence.

## 5. Cancelled Transactions

A cancelled invoice was identified by an invoice number beginning with the letter C.

After duplicate removal, 9,251 cancelled invoice records were identified.

These records were excluded from ordinary product sales.

Two unusually large original transactions were also investigated:

- Invoice 541431: 74,215 units at £1.04 each.
- Invoice 581483: 80,995 units at £2.08 each.

Both had corresponding cancellation invoices shortly afterwards, with matching customer, product, quantity and unit price.

The original transactions were therefore excluded from completed product sales and retained in the returns and adjustments dataset.

Other possible sale-and-cancellation matches were not automatically removed because matching products, quantities and prices alone did not establish a reliable one-to-one relationship.

## 6. Negative Quantities

A total of 10,587 records had negative quantities.

These consisted of:

- 9,251 records associated with cancelled invoices.
- 1,336 negative-quantity records without the cancellation prefix.

The 1,336 additional records had zero unit prices and descriptions that included entries such as damaged goods, checks and stock-related adjustments.

They were retained in the returns and adjustments dataset rather than treated as ordinary sales.

Negative quantities were not automatically assumed to represent customer returns because the descriptions suggest that some may relate to other operational adjustments.

## 7. Zero and Negative Unit Prices

A total of 2,510 records had a unit price of zero:

- 1,174 had positive quantities.
- 1,336 had negative quantities.

These records were retained in the cleaned dataset but excluded from ordinary sales calculations because they do not generate positive sales revenue.

Two records had negative unit prices. Both were associated with the description "Adjust bad debt".

These were treated as accounting adjustments rather than ordinary product sales.

## 8. Administrative Records

Some stock codes represented administrative or non-standard transaction entries rather than ordinary products.

The following codes were separated from ordinary product sales:

- DOT
- POST
- AMAZONFEE
- B
- BANK CHARGES
- M

Stock codes were converted to uppercase and stripped of surrounding spaces before classification.

Manual entries require caution because not every manually entered record can automatically be assumed to be an administrative transaction. These records were separated according to the project's classification rule and should be interpreted with that limitation in mind.

## 9. Extreme Values

The dataset contained unusually large quantities and unit prices.

The two largest quantity transactions were investigated individually and confirmed to have corresponding cancellations.

Other unusual values were not automatically removed simply because they were extreme. Removing records based only on statistical thresholds could exclude genuine transactions.

Further analysis should therefore consider unusual values in context rather than treating every extreme observation as an error.

## 10. Final Dataset Classification

After cleaning and classification, the 536,641 remaining records were divided into three groups:

| Dataset | Records |
|---|---:|
| Product sales | 522,712 |
| Administrative records | 2,607 |
| Returns and adjustments | 11,322 |
| **Total** | **536,641** |

All records were accounted for, and the three groups were mutually exclusive under the classification rules.

## 11. Final Sales Dataset Validation

The final product sales dataset contained:

- Records: 522,712
- Missing product descriptions: 0
- Missing customer IDs: 131,428
- Non-positive quantities: 0
- Non-positive unit prices: 0
- Cancellation invoices: 0
- Missing calculated line values: 0
- Unique identified customers: 4,334
- Total recorded sales value: £10,009,365.98

The sales value was calculated by multiplying quantity by unit price for each retained sales record and summing the resulting line values.

Customer-level analysis will use records with available customer IDs, while overall sales analysis can include sales records without customer identification.

## 12. Limitations and Assumptions

The cleaning process involved several decisions that should be considered when interpreting the results:

1. Exact duplicate rows were removed. This assumes that identical transaction rows represent duplicate records rather than separate legitimate transactions.
2. Records without customer IDs were retained for overall sales analysis but cannot be reliably used for identified customer-level analysis.
3. Negative-quantity transactions were classified as returns and adjustments without assuming that every record represents a customer return.
4. Administrative stock codes were separated using an explicit list. Some manual entries may require further investigation.
5. Extreme values were investigated where possible, but other unusual observations were retained unless there was supporting evidence for exclusion.
6. The analysis uses recorded transaction values and does not establish the retailer's accounting profit, operating costs or actual cash received.

## 13. Conclusion

The cleaning process reduced the dataset from 541,909 to 536,641 records by removing exact duplicates and separating ordinary product sales from administrative entries and returns or adjustments.

The resulting product sales dataset contains 522,712 records with positive quantities and positive unit prices.

The cleaned data is now prepared for analysis of sales performance, product demand, geographical sales patterns and customer purchasing behaviour.

The original dataset has been preserved so that the cleaning decisions remain traceable and reproducible.
