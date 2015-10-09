DROP TABLE IF EXISTS qwi;

CREATE TABLE qwi (
    periodicity   TEXT,     -- Periodicity of report
    seasonadj     TEXT,     -- Seasonal Adjustment Indicator
    geo_level     TEXT,     -- Group: Geographic level of aggregation
    geography     TEXT,     -- Group: Geography code
    ind_level     TEXT,     -- Group: Industry level of aggregation
    industry      TEXT,     -- Group: Industry code
    ownercode     TEXT,     -- Group: Ownership group code
    sex           TEXT,     -- Group: Gender code
    agegrp        TEXT,     -- Group: Age group code (WIA)
    race          TEXT,     -- Group: race
    ethnicity     TEXT,     -- Group: ethnicity
    education     TEXT,     -- Group: education
    firmage       TEXT,     -- Group: Firm Age group
    firmsize      TEXT,     -- Group: Firm Size group
    year          INTEGER,  -- Time: Year
    quarter       INTEGER,  -- Time: Quarter
    Emp           INTEGER,  -- Employment: Counts
    EmpEnd        INTEGER,  -- Employment end-of-quarter: Counts
    EmpS          INTEGER,  -- Employment stable jobs: Counts
    EmpTotal      INTEGER,  -- Employment reference quarter: Counts
    EmpSpv        INTEGER,  -- Employment stable jobs - previous quarter: Counts
    HirA          INTEGER,  -- Hires All: Counts
    HirN          INTEGER,  -- Hires New: Counts
    HirR          INTEGER,  -- Hires Recalls: Counts
    Sep           INTEGER,  -- Separations: Counts
    HirAEnd       INTEGER,  -- End-of-quarter hires
    SepBeg        INTEGER,  -- Beginning-of-quarter separations
    HirAEndRepl   INTEGER,  -- Replacement hires
    HirAEndR      REAL,     -- End-of-quarter hiring rate
    SepBegR       REAL,     -- Beginning-of-quarter separation rate
    HirAEndReplR  REAL,     -- Replacement hiring rate
    HirAS         INTEGER,  -- Hires All stable jobs: Counts
    HirNS         INTEGER,  -- Hires New stable jobs: Counts
    SepS          INTEGER,  -- Separations stable jobs: Counts
    SepSnx        INTEGER,  -- Separations stable jobs - next quarter: Counts
    TurnOvrS      REAL,     -- Turnover stable jobs: Ratio
    FrmJbGn       INTEGER,  -- Firm Job Gains: Counts
    FrmJbLs       INTEGER,  -- Firm Job Loss: Counts
    FrmJbC        INTEGER,  -- Firm jobs change: Net Change
    FrmJbGnS      INTEGER,  -- Firm Gain stable jobs: Counts
    FrmJbLsS      INTEGER,  -- Firm Loss stable jobs: Counts
    FrmJbCS       INTEGER,  -- Firm stable jobs change: Net Change
    EarnS         REAL,     -- Employees stable jobs: Average monthly earnings
    EarnBeg       REAL,     -- Employees beginning-of-quarter : Average monthly earnings
    EarnHirAS     REAL,     -- Hires All stable jobs: Average monthly earnings
    EarnHirNS     REAL,     -- Hires New stable jobs: Average monthly earnings
    EarnSepS      REAL,     -- Separations stable jobs: Average monthly earnings
    Payroll       INTEGER,  -- Total quarterly payroll: Sum
    sEmp          INTEGER,  -- Status: Employment: Counts
    sEmpEnd       INTEGER,  -- Status: Employment end-of-quarter: Counts
    sEmpS         INTEGER,  -- Status: Employment stable jobs: Counts
    sEmpTotal     INTEGER,  -- Status: Employment reference quarter: Counts
    sEmpSpv       INTEGER,  -- Status: Employment stable jobs - previous quarter: Counts
    sHirA         INTEGER,  -- Status: Hires All: Counts
    sHirN         INTEGER,  -- Status: Hires New: Counts
    sHirR         INTEGER,  -- Status: Hires Recalls: Counts
    sSep          INTEGER,  -- Status: Separations: Counts
    sHirAEnd      INTEGER,  -- Status: End-of-quarter hires
    sSepBeg       INTEGER,  -- Status: Beginning-of-quarter separations
    sHirAEndRepl  INTEGER,  -- Status: Replacement hires
    sHirAEndR     INTEGER,  -- Status: End-of-quarter hiring rate
    sSepBegR      INTEGER,  -- Status: Beginning-of-quarter separation rate
    sHirAEndReplR INTEGER,  -- Status: Replacement hiring rate
    sHirAS        INTEGER,  -- Status: Hires All stable jobs: Counts
    sHirNS        INTEGER,  -- Status: Hires New stable jobs: Counts
    sSepS         INTEGER,  -- Status: Separations stable jobs: Counts
    sSepSnx       INTEGER,  -- Status: Separations stable jobs - next quarter: Counts
    sTurnOvrS     INTEGER,  -- Status: Turnover stable jobs: Ratio
    sFrmJbGn      INTEGER,  -- Status: Firm Job Gains: Counts
    sFrmJbLs      INTEGER,  -- Status: Firm Job Loss: Counts
    sFrmJbC       INTEGER,  -- Status: Firm jobs change: Net Change
    sFrmJbGnS     INTEGER,  -- Status: Firm Gain stable jobs: Counts
    sFrmJbLsS     INTEGER,  -- Status: Firm Loss stable jobs: Counts
    sFrmJbCS      INTEGER,  -- Status: Firm stable jobs change: Net Change
    sEarnS        INTEGER,  -- Status: Employees stable jobs: Average monthly earnings
    sEarnBeg      INTEGER,  -- Status: Employees beginning-of-quarter : Average monthly earnings
    sEarnHirAS    INTEGER,  -- Status: Hires All stable jobs: Average monthly earnings
    sEarnHirNS    INTEGER,  -- Status: Hires New stable jobs: Average monthly earnings
    sEarnSepS     INTEGER,  -- Status: Separations stable jobs: Average monthly earnings
    sPayroll      INTEGER,   -- Status: Total quarterly payroll: Sum
    PRIMARY KEY (geography, industry, sex, education, year, quarter)
);
