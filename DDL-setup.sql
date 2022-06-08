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
    QuestionId int,
    Survey int,
    question varchar(100),
    qtype int,
    profChar varchar(50),
    Primary Key (QuestionId, Survey),
    FOREIGN KEY (Survey) REFERENCES Survey(SurveyID),
    FOREIGN KEY (qtype) REFERENCES questionType(Id)
);


create table Possibilities (
    qtype int,
    survey int,
    QuestionNo int,
    ResponseID int,
    TextPrompt varchar(100),
    Primary KEY (survey, QuestionNo, ResponseID),
    FOREIGN KEY (qtype) REFERENCES questionType(Id),
    FOREIGN KEY (survey) REFERENCES Survey(SurveyID)
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
    ProfileID int Primary key,
    UserID int,
    SurveyID int,
    FOREIGN KEY (SurveyID) REFERENCES Survey(SurveyID),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
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

create table ONetJobs (
    Title varchar(50) Primary key,
    Description varchar(100),
    Link varchar(100),
    isStem boolean
);

create table SurveyResponse (
    SurvResp int Primary key,
    User int,
    SurveyId int,
    FOREIGN KEY (User) REFERENCES User(UserID),
    FOREIGN KEY (SurveyID) REFERENCES Survey(SurveyID)
);

create table Responses (
    SurvResp int,
    surveyType int,
    QuestionNo int,
    QValue int,
    primary key (survResp, QuestionNo),
    FOREIGN KEY (SurvResp) REFERENCES SurveyResponse(SurvResp),
    FOREIGN KEY (surveyType, QuestionNo) REFERENCES Questions(Survey, QuestionId)
);
create table UREProfiles(
    ProfileID int Primary key,
    UserID int,
    SurveyID int,
    FOREIGN KEY (SurveyID) REFERENCES Survey(SurveyID),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);
create table UREProfilesval(
    profileId int,
    charId int,
    val float,
    primary key (profileId, charId),
    FOREIGN key (profileId) REFERENCES UREProfiles(ProfileID)
);

create table ONetJobChars(
    Title varchar(60),
    charId int,
    val int,
    primary key (Title, charId),
    foreign key (charId) references profileChars(Id)
);

create table DesiredProfilesMatch(
    profileId int,
    ranking Int,
    Title varchar(50),
    Similarity float,
    primary key (profileId, ranking),
    FOREIGN KEY (profileId) REFERENCES DesProfiles(ProfileId)
);

create table UREProfilesMatch(
    profileId int,
    ranking Int,
    Title varchar(50),
    Similarity float,
    primary key (profileId, ranking),
    FOREIGN KEY (profileId) REFERENCES UREProfiles(ProfileID)
);
create table ProfProfilesMatch(
    profileId int,
    ranking Int,
    Title char(32),
    Similarity float,
    primary key (profileId, ranking),
    FOREIGN KEY (profileId) REFERENCES ProfProfiles(ProfileID)
);