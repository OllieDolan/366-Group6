create table User(
    UserID int Primary key,
    Email char(64)
)

create table UREProfiles(
    ProfileID int Primary key,
    Characteristics char(32),
    Job char(32),
    Survey int,
    FOREIGN KEY (Survey) REFERENCES SurveyResponse(ID)
)

create table ProfProfiles(
    ProfileID int Primary key,
    Status char(32),
    Characteristics char(32),
    Qualifer char(32),
    Experience char(32),
    Survey int,
    FOREIGN KEY (Survey) REFERENCES SurveyResponse(ID)
)

create table DesProfiles (
    ProfileID int Primary key,
    Characteristics char(32),
    User int,
    Ranking int,
    Importance int,
    FOREIGN KEY (User) REFERENCES Users(UserID)
)

create table OnetProfiles (
    ProfileID int Primary key,
    Ranking int,
    Discipline varchar(100)
    UNIQUE (ProfileID, Ranking)
)

create table OnetJobs (
    Title char(32) Primary key,
    Description varchar(100),
    isStem boolean
)

create table OnetData (
    Title char(32),
    Education char(64),
    Training char(64),
    SVP int,
    FOREIGN KEY (Title) REFERENCES OnetJobs(Title)
)

create table SurveyResponse (
    SurvResp int Primary key,
    User int,
    SurveyID int,
    Discipline char(32),
    FOREIGN KEY (User) REFERENCES Users(UserID)
)

create table Responses (
    SurvResp int,
    QuestionNo int,
    Answer varchar(100)
    FOREIGN KEY (SurvResp) REFERENCES SurveyResponse(SurvResp)
)

create table Survey (
    SurveyID int Primary Key,
    Description varchar(100),
)

create table Questions (
    QuestionNo int Primary Key,
    TextPrompt varchar(100),
    Survey int,
    FOREIGN KEY (Survey) REFERENCES Survey(SurveyID)
)

create table Possibilities (
    ResponseID int Primary Key,
    QuestionNo int,
    TextPrompt varchar(100)
    FOREIGN KEY (QuestionNo) REFERENCES Questions(QuestionNo)
)

create table Dimensions (
    DID int Primary Key,
    Name varchar(32),
    Description varchar(100)
)

create table ProfDimensions (
    Dimension int,
    Value int,
    Importance int,
    FOREIGN KEY (Dimension) REFERENCES Dimensions(DID),
    UNIQUE (Dimension, Value, Importance)
)