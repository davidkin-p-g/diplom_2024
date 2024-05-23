(define (problem navigate_robot)
  (:domain robot_navigation)
  (:objects
    loc-0-0 loc-0-1 loc-0-2 loc-1-0 loc-1-1 loc-1-2 loc-2-0 loc-2-1 loc-2-2 - location
    robot - location
  )
  (:init
    (at robot loc-0-0)
    (connected loc-0-0 loc-0-1) (connected loc-0-1 loc-0-2)
    (connected loc-0-0 loc-1-0) (connected loc-1-0 loc-2-0)
    (connected loc-1-0 loc-1-1) (connected loc-1-1 loc-1-2)
    (connected loc-2-0 loc-2-1) (connected loc-2-1 loc-2-2)
    (connected loc-0-2 loc-1-2) (connected loc-1-2 loc-2-2)
    (clear loc-0-1) (clear loc-0-2)
    (clear loc-1-0) (clear loc-1-1) (clear loc-1-2)
    (clear loc-2-0) (clear loc-2-1) (clear loc-2-2)
    (= (distance loc-0-0 loc-0-1) 1)
    (= (distance loc-0-1 loc-0-2) 1)
    (= (distance loc-0-0 loc-1-0) 1)
    (= (distance loc-1-0 loc-2-0) 1)
    (= (distance loc-1-0 loc-1-1) 1)
    (= (distance loc-1-1 loc-1-2) 1)
    (= (distance loc-2-0 loc-2-1) 1)
    (= (distance loc-2-1 loc-2-2) 1)
    (= (distance loc-0-2 loc-1-2) 1)
    (= (distance loc-1-2 loc-2-2) 1)
  )
  (:goal (and (at robot loc-2-2) (mission_completed)))
  (:metric minimize (total-distance))
)