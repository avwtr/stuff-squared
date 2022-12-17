//
//  extensions.swift
//  trivia
//
//  Created by Alex Vawter on 12/16/22.
//
import Foundation
import SwiftUI


extension Text {
    func titleText () -> some View{
        self.font(.system(size: 35, weight:.medium, design: .default)).foregroundColor(Color("AccentColor"))
    }
}
