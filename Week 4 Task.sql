use lms_db;
SELECT
    u.user_id,
    e.course_id,
    a.max_score,
    s.assessment_id,
    s.submitted_at
FROM lms.Users u
JOIN lms.Enrollments e
    ON u.user_id = e.user_id
LEFT JOIN lms.Assessment_Submissions s
    ON u.user_id = s.user_id
LEFT JOIN lms.Assessments a
    ON s.assessment_id = a.assessment_id;


SELECT
    u.user_id,
    u.email,
    u.created_at AS created_date,
    e.enrolled_at AS enrollment_date,
    e.course_id
FROM lms.Users u
JOIN lms.Enrollments e
    ON u.user_id = e.user_id;

    
SELECT
    ua.user_id,
    ua.activity_type,
    l.course_id,
    l.lesson_title
FROM lms.User_Activity ua
JOIN lms.Lessons l
    ON ua.lesson_id = l.lesson_id;


   










