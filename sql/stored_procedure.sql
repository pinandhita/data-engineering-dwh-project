CREATE PROCEDURE DailyTransaction
    @start_date DATE,
    @end_date DATE
AS
BEGIN
    SELECT 
        CAST(TransactionDate AS DATE) AS TransactionDate,
        COUNT(*) AS TotalTransactions,
        SUM(Amount) AS TotalAmount
    FROM FactTransaction
    WHERE CAST(TransactionDate AS DATE) 
          BETWEEN @start_date AND @end_date
    GROUP BY CAST(TransactionDate AS DATE)
    ORDER BY TransactionDate;
END;

EXEC DailyTransaction 
    @start_date = '2024-01-18',
    @end_date = '2024-01-20';

CREATE PROCEDURE BalancePerCustomer
    @name VARCHAR(100)
AS
BEGIN
    SELECT 
        dc.CustomerName,
        da.AccountType,
        da.Balance,
        da.Balance +
        SUM(
            CASE 
                WHEN ft.TransactionType = 'Deposit' THEN ft.Amount
                ELSE -ft.Amount
            END
        ) AS CurrentBalance
    FROM DimCustomer dc
    JOIN DimAccount da 
        ON dc.CustomerID = da.CustomerID
    JOIN FactTransaction ft 
        ON da.AccountID = ft.AccountID
    WHERE dc.CustomerName = @name
      AND da.Status = 'active'
    GROUP BY 
        dc.CustomerName,
        da.AccountType,
        da.Balance;
END;

EXEC BalancePerCustomer 
    @name = 'SHELLY JUWITA';