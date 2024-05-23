(define (domain robot_navigation)
  (:requirements :strips :typing :fluents :durative-actions)
  (:types location)
  (:predicates
    (at ?robot - location)
    (connected ?from - location ?to - location)
    (clear ?loc - location)
    (mission_completed)
  )
  (:functions (distance ?from - location ?to - location) (total-distance))
  
  (:action move
    :parameters (?robot - location ?from - location ?to - location)
    :precondition (and (at ?robot ?from) (connected ?from ?to) (clear ?to))
    :effect (and (at ?robot ?to) (not (at ?robot ?from)))
  )
  
  (:durative-action move_with_cost
    :parameters (?robot - location ?from - location ?to - location)
    :duration (= ?duration (/ (distance ?from ?to) 1.0))
    :condition (and (at start (at ?robot ?from)) (at start (connected ?from ?to)) (at start (clear ?to)))
    :effect (and (at end (at ?robot ?to)) (at end (not (at ?robot ?from))) (at end (increase (total-distance) (distance ?from ?to))))
  )
  
  (:action finish_mission
    :parameters (?robot - location ?end - location)
    :precondition (at ?robot ?end)
    :effect (mission_completed)
  )
)
