create table User(
    UserID int Primary key,
    name varchar(40),
    Email varchar(64)
);

-- Profile characteristics table
create table profileChars(
    Id int Primary key,
    dimension varchar(30),
    characteristics varchar(50) UNIQUE,
    descrp varchar(200)
);

create table Survey (
    SurveyID int Primary Key,
    shortName varchar(30),
    name varchar(60),
    Description varchar(150)
);
create table questionType(
    Id int Primary key
);
create table Questions (
    Survey int,
    QuestionId int Primary Key,
    question varchar(100),
    qtype int,
    profChar varchar(50),
    FOREIGN KEY (Survey) REFERENCES Survey(SurveyID),
    FOREIGN key (qtype) REFERENCES questionType(Id),
    FOREIGN key (profChar) REFERENCES profileChars(characteristics)
);


create table Possibilities (
    qtype int,
    survey int,
    QuestionNo int,
    ResponseID int,
    TextPrompt varchar(100),
    Primary key (survey, QuestionNo, ResponseID),
    FOREIGN KEY (QuestionNo) REFERENCES Questions(QuestionNo),
    FOREIGN key (qtype) REFERENCES questionType(Id),
    FOREIGN key (survey) REFERENCES Survey(SurveyID)
);

create table charValue(
    profileId int,
    charId int,
    charVal int,
    importance int,
    Primary key(profileId, charId),
    FOREIGN KEY (charId) REFERENCES profileChars(Id)
);

create table ProfProfiles(
    ProfileID int Primary key
);
create table ProfProfilesVal(
    profileId int,
    charId int,
    val float,
    primary key (profileId, charId),
    FOREIGN key (profileId) REFERENCES ProfProfiles(ProfileID)
);


create table DesProfiles (
    ProfileID int Primary key,
    profName varchar(32),
    User int,
    FOREIGN key (user) REFERENCES User(UserId)
);

create table OnetProfiles (
    ProfileID int Primary key,
    Ranking int,
    Discipline varchar(100)
);

create table OnetJobs (
    Title char(32) Primary key,
    Description varchar(100),
    Link varchar(100),
    isStem boolean
);

create table OnetData (
    Title char(32),
    Education char(64),
    Training char(64),
    SVP int,
    FOREIGN KEY (Title) REFERENCES OnetJobs(Title)
);

create table SurveyResponse (
    SurvResp int Primary key,
    User int,
    SurveyId int,
    FOREIGN KEY (User) REFERENCES User(UserID)
    FOREIGN KEY (SurveyId) REFERENCES Survey(SurveyID)
);

create table Responses (
    SurvResp int,
    QuestionNo int,
    QValue int,
    primary key (survResp,QuestionNo),
    FOREIGN KEY (SurvResp) REFERENCES SurveyResponse(SurvResp),
    FOREIGN KEY (QuestionNo) REFERENCES Questions(QuestionId)
);
create table UREProfiles(
    ProfileID int Primary key,
    Survey int,
    FOREIGN KEY (Survey) REFERENCES SurveyResponse(SurvResp)
);
