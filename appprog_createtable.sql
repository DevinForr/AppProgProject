-- Instructors table
CREATE TABLE Instructors (
    InstructorID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Department VARCHAR(255),
    Email VARCHAR(255) NOT NULL
);

-- Courses table
CREATE TABLE Courses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Code VARCHAR(255) NOT NULL
);

-- Blocks table
CREATE TABLE Blocks (
    BlockID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    InstructorID INT,
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID)
);

-- Block Timesheet table
CREATE TABLE BlockTimesheets (
    TimesheetID INT PRIMARY KEY AUTO_INCREMENT,
    StartTime INT NOT NULL,
    EndTime INT NOT NULL,
    DayOfWeek CHAR(3) NOT NULL,
    CourseID INT,
    BlockID INT,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (BlockID) REFERENCES Blocks(BlockID)
);

-- Programs table
CREATE TABLE Programs (
    ProgramID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Type VARCHAR(255) NOT NULL,
    BlockID INT,
    CourseID INT,
    FOREIGN KEY (BlockID) REFERENCES Blocks(BlockID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- Students table
CREATE TABLE Students (
    StudentID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL,
    ProgramID INT,
    FOREIGN KEY (ProgramID) REFERENCES Programs(ProgramID)
);

-- Enrollment table
CREATE TABLE Enrollments (
    EnrollmentID INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT,
    BlockID INT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (BlockID) REFERENCES Blocks(BlockID)
);