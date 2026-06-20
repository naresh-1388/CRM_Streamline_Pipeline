SELECT

    COUNT(*)  AS TOTAL_CUSTOMERS

FROM {{ ref('dim_customers') }}