//
//  answer.swift
//  trivia
//
//  Created by Alex Vawter on 12/16/22.
//

import Foundation


struct Answer: Identifiable{
    var id = UUID()
    var text: AttributedString
    var isCorrect: Bool
}
