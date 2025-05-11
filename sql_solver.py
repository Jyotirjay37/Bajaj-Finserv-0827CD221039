#!/usr/bin/env python3

def solve_sql_problem(problem_number):
    if problem_number == 1:
        return solve_problem_1()
    else:
        return solve_problem_2()

def solve_problem_1():
    sql_query = """
    SELECT 
        p.AMOUNT AS SALARY,
        CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
        YEAR(CURRENT_DATE) - YEAR(e.DOB) - 
            CASE WHEN MONTH(CURRENT_DATE) < MONTH(e.DOB) OR 
                     (MONTH(CURRENT_DATE) = MONTH(e.DOB) AND DAY(CURRENT_DATE) < DAY(e.DOB))
                 THEN 1
                 ELSE 0
            END AS AGE,
        d.DEPARTMENT_NAME
    FROM PAYMENTS p
    JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
    JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
    WHERE DAY(p.PAYMENT_TIME) != 1
    ORDER BY p.AMOUNT DESC
    LIMIT 1;
    """
    return sql_query

def solve_problem_2():
    sql_query = """
    SELECT 
        e1.EMP_ID,
        e1.FIRST_NAME,
        e1.LAST_NAME,
        d.DEPARTMENT_NAME,
        COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
    FROM EMPLOYEE e1
    JOIN DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID
    LEFT JOIN EMPLOYEE e2 ON e1.DEPARTMENT = e2.DEPARTMENT 
        AND e1.DOB > e2.DOB
    GROUP BY e1.EMP_ID, e1.FIRST_NAME, e1.LAST_NAME, d.DEPARTMENT_NAME
    ORDER BY e1.EMP_ID DESC;
    """
    return sql_query