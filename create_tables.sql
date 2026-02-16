-- Create database if not exists
CREATE DATABASE IF NOT EXISTS finance_xai_db;
USE finance_xai_db;

-- Table for stock data
CREATE TABLE IF NOT EXISTS real_market_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    symbol VARCHAR(20) NOT NULL,
    company_name VARCHAR(100),
    open DECIMAL(10,2),
    high DECIMAL(10,2),
    low DECIMAL(10,2),
    close DECIMAL(10,2),
    volume BIGINT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for economic data
CREATE TABLE IF NOT EXISTS economic_indicators (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    indicator_id VARCHAR(20),
    value DECIMAL(15,4),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for loan data
CREATE TABLE IF NOT EXISTS real_loans (
    id INT AUTO_INCREMENT PRIMARY KEY,
    loan_id VARCHAR(50),
    loan_amnt DECIMAL(10,2),
    int_rate DECIMAL(5,4),
    is_default BOOLEAN DEFAULT FALSE
);

SHOW TABLES;